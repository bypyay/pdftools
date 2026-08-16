import os

base_dir = r"D:\Codding\Claude Cowork code\PDF Tools"
tools_dir = os.path.join(base_dir, "image-tools")
js_dir = os.path.join(base_dir, "assets", "js", "image-tools")

# 1. watermark-image
watermark_php = """<?php
$root = '../../';
$page_title = 'Watermark Image Online Free — Add Text & Logo to Photos | Daily1Step';
$page_description = 'Add text watermark or logo image to your pictures online. Click and drag watermark with cursor. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Watermark Image</h1>
      <p>Stamp text or your brand logo on pictures with interactive click & drag positioning.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:960px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 340px; gap:24px; align-items:start;" class="watermark-grid">
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <h4 style="margin:0 0 12px; font-size:.95rem; color:var(--ink);">Click & Drag Watermark on Preview</h4>
          <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b;">
            <canvas id="previewCanvas" style="max-width:100%; max-height:420px; display:block; cursor:move;"></canvas>
          </div>
        </div>

        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:14px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Watermark Text</label>
            <input type="text" id="wmText" value="CONFIDENTIAL" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Text Color</label>
            <input type="color" id="wmColor" value="#ffffff" style="width:100%; height:40px; border:1.5px solid var(--border); border-radius:8px; cursor:pointer;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Opacity</label>
            <input type="range" id="wmOpacity" min="10" max="100" value="50" style="width:100%;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Font Size</label>
            <input type="range" id="wmSize" min="16" max="100" value="42" style="width:100%;">
          </div>
          <button class="btn" id="downloadBtn" style="margin-top:8px;">Download Watermarked Image</button>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
@media (max-width: 768px) {
  .watermark-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/watermark-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""

os.makedirs(os.path.join(tools_dir, "watermark-image"), exist_ok=True)
with open(os.path.join(tools_dir, "watermark-image", "index.php"), "w", encoding="utf-8") as f:
    f.write(watermark_php)

watermark_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var wmText = document.getElementById('wmText');
  var wmColor = document.getElementById('wmColor');
  var wmOpacity = document.getElementById('wmOpacity');
  var wmSize = document.getElementById('wmSize');
  var downloadBtn = document.getElementById('downloadBtn');

  var loadedImg = null;
  var currentFile = null;
  var posX = 100, posY = 100;
  var isDragging = false, startX = 0, startY = 0;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    currentFile = file;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
        canvas.width = img.naturalWidth || img.width;
        canvas.height = img.naturalHeight || img.height;
        posX = canvas.width / 2;
        posY = canvas.height / 2;
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
        render();
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  function render() {
    if (!loadedImg) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(loadedImg, 0, 0);

    var text = wmText.value || 'WATERMARK';
    var size = parseInt(wmSize.value) || 42;
    var opacity = (parseInt(wmOpacity.value) || 50) / 100;

    ctx.save();
    ctx.globalAlpha = opacity;
    ctx.fillStyle = wmColor.value;
    ctx.font = 'bold ' + size + 'px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.shadowColor = 'rgba(0,0,0,0.5)';
    ctx.shadowBlur = 6;
    ctx.fillText(text, posX, posY);
    ctx.restore();
  }

  wmText.addEventListener('input', render);
  wmColor.addEventListener('input', render);
  wmOpacity.addEventListener('input', render);
  wmSize.addEventListener('input', render);

  canvas.addEventListener('mousedown', function (e) {
    isDragging = true;
    var rect = canvas.getBoundingClientRect();
    var scaleX = canvas.width / rect.width;
    var scaleY = canvas.height / rect.height;
    posX = (e.clientX - rect.left) * scaleX;
    posY = (e.clientY - rect.top) * scaleY;
    render();
  });
  window.addEventListener('mousemove', function (e) {
    if (!isDragging || !loadedImg) return;
    var rect = canvas.getBoundingClientRect();
    var scaleX = canvas.width / rect.width;
    var scaleY = canvas.height / rect.height;
    posX = (e.clientX - rect.left) * scaleX;
    posY = (e.clientY - rect.top) * scaleY;
    render();
  });
  window.addEventListener('mouseup', function () { isDragging = false; });

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

  downloadBtn.addEventListener('click', function () {
    render();
    canvas.toBlob(function (blob) {
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'watermarked-image.jpg';
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "watermark-image.js"), "w", encoding="utf-8") as f:
    f.write(watermark_js)

# 2. rotate-flip-image
rotate_php = """<?php
$root = '../../';
$page_title = 'Rotate & Flip Image Online Free | Daily1Step';
$page_description = 'Rotate image 90, 180, 270 degrees or flip horizontally and vertically online. 100% free and client-side.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Rotate & Flip Image</h1>
      <p>Rotate photos 90°, 180°, 270° or mirror flip horizontally and vertically in 1 click.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <div style="display:flex; justify-content:center; gap:10px; margin-bottom:20px; flex-wrap:wrap;">
          <button type="button" class="btn secondary" id="rotLeftBtn">&#8634; Rotate Left 90°</button>
          <button type="button" class="btn secondary" id="rotRightBtn">&#8635; Rotate Right 90°</button>
          <button type="button" class="btn secondary" id="flipHBtn">&#8644; Flip Horizontal</button>
          <button type="button" class="btn secondary" id="flipVBtn">&#8645; Flip Vertical</button>
        </div>

        <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#fff; box-shadow:var(--shadow-sm);">
          <canvas id="previewCanvas" style="max-width:100%; max-height:420px; display:block;"></canvas>
        </div>

        <div style="margin-top:20px;">
          <button class="btn" id="downloadBtn">Download Transformed Image</button>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/rotate-flip-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""

os.makedirs(os.path.join(tools_dir, "rotate-flip-image"), exist_ok=True)
with open(os.path.join(tools_dir, "rotate-flip-image", "index.php"), "w", encoding="utf-8") as f:
    f.write(rotate_php)

rotate_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var rotLeftBtn = document.getElementById('rotLeftBtn');
  var rotRightBtn = document.getElementById('rotRightBtn');
  var flipHBtn = document.getElementById('flipHBtn');
  var flipVBtn = document.getElementById('flipVBtn');
  var downloadBtn = document.getElementById('downloadBtn');

  var loadedImg = null;
  var currentAngle = 0;
  var flipH = 1, flipV = 1;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
        currentAngle = 0;
        flipH = 1; flipV = 1;
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
        render();
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  function render() {
    if (!loadedImg) return;
    var rad = (currentAngle * Math.PI) / 180;
    var sin = Math.abs(Math.sin(rad));
    var cos = Math.abs(Math.cos(rad));
    var origW = loadedImg.naturalWidth || loadedImg.width;
    var origH = loadedImg.naturalHeight || loadedImg.height;

    var newW = Math.round(origW * cos + origH * sin);
    var newH = Math.round(origW * sin + origH * cos);
    canvas.width = newW;
    canvas.height = newH;

    ctx.save();
    ctx.translate(newW / 2, newH / 2);
    ctx.rotate(rad);
    ctx.scale(flipH, flipV);
    ctx.drawImage(loadedImg, -origW / 2, -origH / 2);
    ctx.restore();
  }

  rotLeftBtn.addEventListener('click', function () { currentAngle = (currentAngle - 90) % 360; render(); });
  rotRightBtn.addEventListener('click', function () { currentAngle = (currentAngle + 90) % 360; render(); });
  flipHBtn.addEventListener('click', function () { flipH *= -1; render(); });
  flipVBtn.addEventListener('click', function () { flipV *= -1; render(); });

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

  downloadBtn.addEventListener('click', function () {
    render();
    canvas.toBlob(function (blob) {
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'transformed-image.jpg';
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "rotate-flip-image.js"), "w", encoding="utf-8") as f:
    f.write(rotate_js)

# 3. blur-censor-image
blur_php = """<?php
$root = '../../';
$page_title = 'Blur & Censor Image Online Free — Pixelate Faces & Text | Daily1Step';
$page_description = 'Blur or pixelate faces, private numbers, and sensitive parts of an image online for free. Interactive drag brush. 100% private.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Blur & Censor Image</h1>
      <p>Hide sensitive data, pixelate faces, or blur private documents with an interactive brush.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:960px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <div style="display:flex; justify-content:center; gap:12px; margin-bottom:16px; flex-wrap:wrap; align-items:center;">
          <button type="button" class="btn secondary active" id="pixelBtn">Pixelate Mode</button>
          <button type="button" class="btn secondary" id="blackoutBtn">Blackout Box</button>
          <button type="button" class="btn secondary" id="clearBtn">Reset Changes</button>
          <button class="btn" id="downloadBtn">Download Censored Image</button>
        </div>

        <p style="font-size:.82rem; color:var(--ink-soft); margin-bottom:12px;">Click and drag over any area on the image to censor it.</p>

        <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b;">
          <canvas id="previewCanvas" style="max-width:100%; max-height:450px; display:block; cursor:crosshair;"></canvas>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/blur-censor-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""

os.makedirs(os.path.join(tools_dir, "blur-censor-image"), exist_ok=True)
with open(os.path.join(tools_dir, "blur-censor-image", "index.php"), "w", encoding="utf-8") as f:
    f.write(blur_php)

blur_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var pixelBtn = document.getElementById('pixelBtn');
  var blackoutBtn = document.getElementById('blackoutBtn');
  var clearBtn = document.getElementById('clearBtn');
  var downloadBtn = document.getElementById('downloadBtn');

  var loadedImg = null;
  var mode = 'pixel'; // 'pixel' or 'blackout'
  var isDrawing = false, startX = 0, startY = 0;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
        canvas.width = img.naturalWidth || img.width;
        canvas.height = img.naturalHeight || img.height;
        ctx.drawImage(img, 0, 0);
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  pixelBtn.addEventListener('click', function () { mode = 'pixel'; pixelBtn.classList.add('active'); blackoutBtn.classList.remove('active'); });
  blackoutBtn.addEventListener('click', function () { mode = 'blackout'; blackoutBtn.classList.add('active'); pixelBtn.classList.remove('active'); });
  clearBtn.addEventListener('click', function () { if (loadedImg) ctx.drawImage(loadedImg, 0, 0); });

  function getCanvasCoords(e) {
    var rect = canvas.getBoundingClientRect();
    return {
      x: (e.clientX - rect.left) * (canvas.width / rect.width),
      y: (e.clientY - rect.top) * (canvas.height / rect.height)
    };
  }

  canvas.addEventListener('mousedown', function (e) {
    isDrawing = true;
    var c = getCanvasCoords(e);
    startX = c.x; startY = c.y;
  });

  window.addEventListener('mouseup', function (e) {
    if (!isDrawing) return;
    isDrawing = false;
    var c = getCanvasCoords(e);
    var x = Math.min(startX, c.x);
    var y = Math.min(startY, c.y);
    var w = Math.abs(c.x - startX);
    var h = Math.abs(c.y - startY);
    if (w < 4 || h < 4) return;

    if (mode === 'blackout') {
      ctx.fillStyle = '#000000';
      ctx.fillRect(x, y, w, h);
    } else {
      // Pixelate effect
      var pixelSize = Math.max(10, Math.round(w / 12));
      var sampleCanvas = document.createElement('canvas');
      sampleCanvas.width = Math.max(1, Math.floor(w / pixelSize));
      sampleCanvas.height = Math.max(1, Math.floor(h / pixelSize));
      var sCtx = sampleCanvas.getContext('2d');
      sCtx.drawImage(canvas, x, y, w, h, 0, 0, sampleCanvas.width, sampleCanvas.height);
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(sampleCanvas, 0, 0, sampleCanvas.width, sampleCanvas.height, x, y, w, h);
      ctx.imageSmoothingEnabled = true;
    }
  });

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

  downloadBtn.addEventListener('click', function () {
    canvas.toBlob(function (blob) {
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'censored-image.jpg';
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "blur-censor-image.js"), "w", encoding="utf-8") as f:
    f.write(blur_js)

# 4. image-color-picker
color_php = """<?php
$root = '../../';
$page_title = 'Image Color Picker Online Free — Extract Hex & RGB from Photos | Daily1Step';
$page_description = 'Pick exact colors and hex/RGB color codes from any image with an interactive eye-dropper cursor. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Image Color Picker</h1>
      <p>Hover and click anywhere on your image to instantly extract and copy HEX, RGB, and HSL color codes.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:960px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 300px; gap:24px; align-items:start;" class="color-grid">
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <h4 style="margin:0 0 12px; font-size:.95rem; color:var(--ink);">Click on image to sample color</h4>
          <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#fff;">
            <canvas id="previewCanvas" style="max-width:100%; max-height:450px; display:block; cursor:crosshair;"></canvas>
          </div>
        </div>

        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:16px;">
          <div style="width:100%; height:80px; border-radius:10px; border:1.5px solid var(--border); box-shadow:var(--shadow-sm);" id="colorSwatch"></div>
          
          <div>
            <label style="display:block; font-weight:700; font-size:.82rem; color:var(--ink-soft); margin-bottom:4px;">HEX CODE</label>
            <div style="display:flex; gap:6px;">
              <input type="text" id="hexVal" readonly style="flex:1; padding:8px 12px; border:1.5px solid var(--border); border-radius:8px; font-weight:700; font-family:monospace; font-size:1.1rem; color:var(--red);">
              <button type="button" class="btn secondary" id="copyHexBtn" style="padding:8px 14px;">Copy</button>
            </div>
          </div>

          <div>
            <label style="display:block; font-weight:700; font-size:.82rem; color:var(--ink-soft); margin-bottom:4px;">RGB CODE</label>
            <div style="display:flex; gap:6px;">
              <input type="text" id="rgbVal" readonly style="flex:1; padding:8px 12px; border:1.5px solid var(--border); border-radius:8px; font-weight:700; font-family:monospace;">
              <button type="button" class="btn secondary" id="copyRgbBtn" style="padding:8px 14px;">Copy</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
@media (max-width: 768px) {
  .color-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/image-color-picker.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""

os.makedirs(os.path.join(tools_dir, "image-color-picker"), exist_ok=True)
with open(os.path.join(tools_dir, "image-color-picker", "index.php"), "w", encoding="utf-8") as f:
    f.write(color_php)

color_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var colorSwatch = document.getElementById('colorSwatch');
  var hexVal = document.getElementById('hexVal');
  var rgbVal = document.getElementById('rgbVal');
  var copyHexBtn = document.getElementById('copyHexBtn');
  var copyRgbBtn = document.getElementById('copyRgbBtn');

  function rgbToHex(r, g, b) {
    return '#' + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1).toUpperCase();
  }

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        canvas.width = img.naturalWidth || img.width;
        canvas.height = img.naturalHeight || img.height;
        ctx.drawImage(img, 0, 0);
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
        sampleAt(Math.floor(canvas.width / 2), Math.floor(canvas.height / 2));
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  function sampleAt(x, y) {
    var p = ctx.getImageData(x, y, 1, 1).data;
    var hex = rgbToHex(p[0], p[1], p[2]);
    var rgb = 'rgb(' + p[0] + ', ' + p[1] + ', ' + p[2] + ')';

    colorSwatch.style.background = hex;
    hexVal.value = hex;
    rgbVal.value = rgb;
  }

  canvas.addEventListener('click', function (e) {
    var rect = canvas.getBoundingClientRect();
    var x = Math.floor((e.clientX - rect.left) * (canvas.width / rect.width));
    var y = Math.floor((e.clientY - rect.top) * (canvas.height / rect.height));
    sampleAt(x, y);
  });

  copyHexBtn.addEventListener('click', function () {
    navigator.clipboard.writeText(hexVal.value);
    copyHexBtn.textContent = 'Copied!';
    setTimeout(function () { copyHexBtn.textContent = 'Copy'; }, 1500);
  });

  copyRgbBtn.addEventListener('click', function () {
    navigator.clipboard.writeText(rgbVal.value);
    copyRgbBtn.textContent = 'Copied!';
    setTimeout(function () { copyRgbBtn.textContent = 'Copy'; }, 1500);
  });

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
})();
"""
with open(os.path.join(js_dir, "image-color-picker.js"), "w", encoding="utf-8") as f:
    f.write(color_js)

# 5. image-to-text-ocr
ocr_php = """<?php
$root = '../../';
$page_title = 'Image to Text (OCR) Online Free — Extract Text from Images | Daily1Step';
$page_description = 'Extract selectable text from photos, scans, and documents using browser-based Optical Character Recognition (OCR). 100% free and private.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Image to Text (OCR)</h1>
      <p>Extract typed or printed text from images, documents, and screenshots instantly.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image containing text</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Supports JPG, PNG, WEBP</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div class="file-row" style="margin-bottom:16px;">
        <span class="name" id="fileName"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div class="actions">
        <button class="btn" id="ocrBtn">Extract Text with OCR</button>
      </div>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Running neural character recognition...</div>
    </div>

    <div class="result-box" id="resultBox" style="text-align:left;">
      <div style="text-align:center;"><div class="check">&#10003;</div><h3>Text Extracted Successfully!</h3></div>
      <textarea id="extractedText" rows="10" style="width:100%; margin:16px 0; padding:14px; border:1.5px solid var(--border); border-radius:8px; font-family:monospace; font-size:.92rem;"></textarea>
      <div style="display:flex; gap:10px; justify-content:center;">
        <button class="btn" id="copyTextBtn">Copy Text</button>
        <a class="btn secondary" id="downloadTxtBtn">Download .TXT</a>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/tesseract.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/image-to-text-ocr.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""

os.makedirs(os.path.join(tools_dir, "image-to-text-ocr"), exist_ok=True)
with open(os.path.join(tools_dir, "image-to-text-ocr", "index.php"), "w", encoding="utf-8") as f:
    f.write(ocr_php)

ocr_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var fileNameEl = document.getElementById('fileName');
  var removeFileBtn = document.getElementById('removeFile');
  var ocrBtn = document.getElementById('ocrBtn');
  var progressWrap = document.getElementById('progressWrap');
  var progressBar = document.getElementById('progressBar');
  var statusText = document.getElementById('statusText');
  var resultBox = document.getElementById('resultBox');
  var extractedText = document.getElementById('extractedText');
  var copyTextBtn = document.getElementById('copyTextBtn');
  var downloadTxtBtn = document.getElementById('downloadTxtBtn');

  var currentFile = null;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    currentFile = file;
    fileNameEl.textContent = file.name;
    dropzone.style.display = 'none';
    editorWrap.style.display = 'block';
  }

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
    dropzone.style.display = 'block';
    editorWrap.style.display = 'none';
  });

  ocrBtn.addEventListener('click', function () {
    if (!currentFile || typeof Tesseract === 'undefined') {
      alert('OCR Engine is loading...');
      return;
    }

    ocrBtn.disabled = true;
    progressWrap.style.display = 'block';
    progressBar.style.width = '25%';
    statusText.textContent = 'Initializing OCR engine...';

    Tesseract.recognize(currentFile, 'eng', {
      logger: function (m) {
        if (m.status === 'recognizing text') {
          progressBar.style.width = Math.round(m.progress * 100) + '%';
          statusText.textContent = 'Extracting text: ' + Math.round(m.progress * 100) + '%';
        }
      }
    }).then(function (res) {
      extractedText.value = res.data.text || 'No text found in image.';
      var blob = new Blob([extractedText.value], { type: 'text/plain;charset=utf-8' });
      downloadTxtBtn.href = URL.createObjectURL(blob);
      downloadTxtBtn.download = currentFile.name.replace(/\\.[^/.]+$/, '') + '.txt';

      progressWrap.style.display = 'none';
      editorWrap.style.display = 'none';
      resultBox.style.display = 'block';
    }).catch(function (err) {
      console.error(err);
      alert('Error during OCR: ' + err.message);
      progressWrap.style.display = 'none';
      ocrBtn.disabled = false;
    });
  });

  copyTextBtn.addEventListener('click', function () {
    navigator.clipboard.writeText(extractedText.value);
    copyTextBtn.textContent = 'Copied!';
    setTimeout(function () { copyTextBtn.textContent = 'Copy Text'; }, 1500);
  });
})();
"""
with open(os.path.join(js_dir, "image-to-text-ocr.js"), "w", encoding="utf-8") as f:
    f.write(ocr_js)

print("Special tools generation complete.")
