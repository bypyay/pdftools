(function () {
  if (window.pdfjsLib) {
    var pdfScriptTag = document.querySelector('script[src*="vendor/pdf.min.js"]');
    var siteRoot = pdfScriptTag ? pdfScriptTag.getAttribute('src').replace(/vendor\/pdf\.min\.js.*$/, '') : '';
    pdfjsLib.GlobalWorkerOptions.workerSrc = siteRoot + 'vendor/pdf.worker.min.js';
  }

  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var fileInfo = document.getElementById('fileInfo');
  var fileNameEl = document.getElementById('fileName');
  var pageCountEl = document.getElementById('pageCount');
  var removeFileBtn = document.getElementById('removeFile');
  var previewWrap = document.getElementById('previewWrap');
  var actions = document.getElementById('actions');
  var applyBtn = document.getElementById('applyBtn');
  var progressWrap = document.getElementById('progressWrap');
  var progressBar = document.getElementById('progressBar');
  var statusText = document.getElementById('statusText');
  var resultBox = document.getElementById('resultBox');
  var resultInfo = document.getElementById('resultInfo');
  var downloadLink = document.getElementById('downloadLink');
  var resetBtn = document.getElementById('resetBtn');
  var continueBox = document.getElementById('continueBox');
  var continueGrid = document.getElementById('continueGrid');

  var wmText = document.getElementById('wmText');
  var wmSize = document.getElementById('wmSize');
  var wmSizeVal = document.getElementById('wmSizeVal');
  var wmOpacity = document.getElementById('wmOpacity');
  var wmOpacityVal = document.getElementById('wmOpacityVal');
  var wmRotation = document.getElementById('wmRotation');
  var wmRotationVal = document.getElementById('wmRotationVal');
  var wmColor = document.getElementById('wmColor');

  var currentFile = null;
  var pageCount = 0;
  var baseCanvas = null;
  var previewCanvas = null;
  var previewScale = 1;

  function hexToRgb(hex) {
    var m = hex.replace('#', '');
    var r = parseInt(m.substring(0, 2), 16);
    var g = parseInt(m.substring(2, 4), 16);
    var b = parseInt(m.substring(4, 6), 16);
    return { r: r, g: g, b: b };
  }

  function loadFile(file) {
    if (!file) return;
    if (file.type !== 'application/pdf' && !/\.pdf$/i.test(file.name)) {
      alert('Please select a PDF file.');
      return;
    }
    currentFile = file;
    file.arrayBuffer().then(function (buf) {
      return pdfjsLib.getDocument({ data: buf }).promise;
    }).then(function (pdf) {
      pageCount = pdf.numPages;
      fileNameEl.textContent = file.name;
      pageCountEl.textContent = pageCount + ' page' + (pageCount === 1 ? '' : 's');
      fileInfo.style.display = 'block';
      actions.style.display = 'block';
      return renderPreviewBase(pdf);
    }).catch(function (err) {
      console.error(err);
      alert('Could not read this PDF. It may be corrupted or password-protected.');
      currentFile = null;
    });
  }

  function renderPreviewBase(pdf) {
    return pdf.getPage(1).then(function (page) {
      var targetWidth = 260;
      var unscaled = page.getViewport({ scale: 1 });
      previewScale = targetWidth / unscaled.width;
      var viewport = page.getViewport({ scale: previewScale });
      baseCanvas = document.createElement('canvas');
      baseCanvas.width = Math.round(viewport.width);
      baseCanvas.height = Math.round(viewport.height);
      var ctx = baseCanvas.getContext('2d');
      return page.render({ canvasContext: ctx, viewport: viewport }).promise.then(function () {
        previewWrap.innerHTML = '';
        previewCanvas = document.createElement('canvas');
        previewCanvas.width = baseCanvas.width;
        previewCanvas.height = baseCanvas.height;
        previewWrap.appendChild(previewCanvas);
        redrawPreview();
      });
    });
  }

  function redrawPreview() {
    if (!baseCanvas || !previewCanvas) return;
    var ctx = previewCanvas.getContext('2d');
    ctx.clearRect(0, 0, previewCanvas.width, previewCanvas.height);
    ctx.drawImage(baseCanvas, 0, 0);

    var text = wmText.value || '';
    if (!text) return;
    var size = parseFloat(wmSize.value) * previewScale;
    var opacity = parseFloat(wmOpacity.value) / 100;
    var rotation = parseFloat(wmRotation.value);
    var rgb = hexToRgb(wmColor.value);

    ctx.save();
    ctx.translate(previewCanvas.width / 2, previewCanvas.height / 2);
    ctx.rotate(-rotation * Math.PI / 180); // canvas rotates clockwise for positive angles; flip to match PDF convention
    ctx.font = size + 'px Helvetica, Arial, sans-serif';
    ctx.fillStyle = 'rgba(' + rgb.r + ',' + rgb.g + ',' + rgb.b + ',' + opacity + ')';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(text, 0, 0);
    ctx.restore();
  }

  [wmText, wmColor].forEach(function (el) { el.addEventListener('input', redrawPreview); });
  wmSize.addEventListener('input', function () { wmSizeVal.textContent = wmSize.value; redrawPreview(); });
  wmOpacity.addEventListener('input', function () { wmOpacityVal.textContent = wmOpacity.value + '%'; redrawPreview(); });
  wmRotation.addEventListener('input', function () { wmRotationVal.innerHTML = wmRotation.value + '&deg;'; redrawPreview(); });

  dropzone.addEventListener('click', function () { fileInput.click(); });
  fileInput.addEventListener('change', function (e) { loadFile(e.target.files[0]); fileInput.value = ''; });
  ['dragenter', 'dragover'].forEach(function (evt) {
    dropzone.addEventListener(evt, function (e) { e.preventDefault(); dropzone.classList.add('dragover'); });
  });
  ['dragleave', 'drop'].forEach(function (evt) {
    dropzone.addEventListener(evt, function (e) { e.preventDefault(); dropzone.classList.remove('dragover'); });
  });
  dropzone.addEventListener('drop', function (e) {
    if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) loadFile(e.dataTransfer.files[0]);
  });

  removeFileBtn.addEventListener('click', function () {
    currentFile = null;
    pageCount = 0;
    fileInfo.style.display = 'none';
    actions.style.display = 'none';
    previewWrap.innerHTML = '';
  });

  applyBtn.addEventListener('click', function () {
    if (!currentFile) return;
    if (!wmText.value) { alert('Enter watermark text.'); return; }
    applyBtn.disabled = true;
    progressWrap.style.display = 'block';
    progressBar.style.width = '0%';
    statusText.textContent = 'Adding watermark...';
    setTimeout(doWatermark, 50);
  });

  function doWatermark() {
    var text = wmText.value;
    var size = parseFloat(wmSize.value);
    var opacity = parseFloat(wmOpacity.value) / 100;
    var rotationDeg = parseFloat(wmRotation.value);
    var rgbHex = hexToRgb(wmColor.value);

    currentFile.arrayBuffer().then(function (buf) {
      return PDFLib.PDFDocument.load(buf, { ignoreEncryption: true });
    }).then(function (doc) {
      return doc.embedFont(PDFLib.StandardFonts.HelveticaBold).then(function (font) {
        var pages = doc.getPages();
        var textWidth = font.widthOfTextAtSize(text, size);
        var halfW = textWidth / 2;
        var halfH = size / 2;
        var theta = rotationDeg * Math.PI / 180;

        pages.forEach(function (page, index) {
          progressBar.style.width = Math.round(((index) / pages.length) * 90) + '%';
          var cx = page.getWidth() / 2;
          var cy = page.getHeight() / 2;
          var x = cx - (halfW * Math.cos(theta) - halfH * Math.sin(theta));
          var y = cy - (halfW * Math.sin(theta) + halfH * Math.cos(theta));
          page.drawText(text, {
            x: x,
            y: y,
            size: size,
            font: font,
            color: PDFLib.rgb(rgbHex.r / 255, rgbHex.g / 255, rgbHex.b / 255),
            opacity: opacity,
            rotate: PDFLib.degrees(rotationDeg)
          });
        });
        return doc.save();
      });
    }).then(function (bytes) {
      var blob = new Blob([bytes], { type: 'application/pdf' });
      var url = URL.createObjectURL(blob);
      downloadLink.href = url;
      resultInfo.textContent = pageCount + ' page' + (pageCount === 1 ? '' : 's') + ' watermarked.';
      progressBar.style.width = '100%';
      progressWrap.style.display = 'none';
      resultBox.style.display = 'block';
      if (window.PdfHandoff && continueBox && continueGrid) {
        PdfHandoff.renderContinueBox(continueGrid, ['merge-pdf', 'split-pdf', 'compress-pdf', 'pdf-to-jpg'], function () {
          return { blob: blob, filename: 'watermarked.pdf' };
        });
        continueBox.style.display = 'block';
      }
    }).catch(function (err) {
      console.error(err);
      statusText.textContent = 'Something went wrong: ' + err.message;
      applyBtn.disabled = false;
    });
  }

  resetBtn.addEventListener('click', function () {
    currentFile = null;
    pageCount = 0;
    fileInfo.style.display = 'none';
    actions.style.display = 'none';
    resultBox.style.display = 'none';
    if (continueBox) continueBox.style.display = 'none';
    applyBtn.disabled = false;
    previewWrap.innerHTML = '';
  });

  if (window.PdfHandoff) {
    PdfHandoff.take().then(function (result) {
      if (result && result.blob) {
        var f = new File([result.blob], result.filename || 'file.pdf', { type: 'application/pdf' });
        loadFile(f);
        PdfHandoff.showBanner('Continuing with ' + (result.filename || 'your file') + ' — set your watermark below.');
      }
    });
  }
})();
