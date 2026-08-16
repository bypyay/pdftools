import os

base_dir = r"D:\Codding\Claude Cowork code\PDF Tools"
tools_dir = os.path.join(base_dir, "image-tools")
js_dir = os.path.join(base_dir, "assets", "js", "image-tools")

# 1. resize-image-cm-mm
cm_php = """<?php
$root = '../../';
$page_title = 'Resize Image in CM / MM / Inches Online Free | Daily1Step';
$page_description = 'Resize photos to exact dimensions in Centimeters, Millimeters, or Inches with custom DPI (200, 300, 600 DPI) for official documents. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Resize Image in CM / MM / Inches</h1>
      <p>Convert real-world print dimensions (cm, mm, inch) to exact pixel dimensions with DPI precision.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px;">
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:14px; margin-bottom:16px;" class="dim-grid">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Unit</label>
            <select id="unitSelect" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
              <option value="cm">Centimeter (cm)</option>
              <option value="mm">Millimeter (mm)</option>
              <option value="inch">Inches (in)</option>
            </select>
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Width</label>
            <input type="number" step="0.1" id="widthInput" value="3.5" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Height</label>
            <input type="number" step="0.1" id="heightInput" value="4.5" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
        </div>

        <div style="margin-bottom:18px;">
          <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Resolution (DPI)</label>
          <div style="display:flex; gap:8px;">
            <button type="button" class="dpi-btn" data-dpi="150">150 DPI</button>
            <button type="button" class="dpi-btn active" data-dpi="300">300 DPI (Standard)</button>
            <button type="button" class="dpi-btn" data-dpi="600">600 DPI (High Res)</button>
          </div>
        </div>

        <button class="btn" id="resizeBtn" style="width:100%;">Resize & Download</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
.dpi-btn {
  background: var(--bg);
  border: 1.5px solid var(--border);
  border-radius: 8px;
  padding: 8px 14px;
  font-weight: 700;
  font-size: .85rem;
  color: var(--ink-soft);
  cursor: pointer;
  flex: 1;
}
.dpi-btn.active {
  background: var(--red-light);
  border-color: var(--red);
  color: var(--red);
}
@media (max-width: 600px) {
  .dim-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/resize-image-cm-mm.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "resize-image-cm-mm"), exist_ok=True)
with open(os.path.join(tools_dir, "resize-image-cm-mm", "index.php"), "w", encoding="utf-8") as f:
    f.write(cm_php)

cm_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var unitSelect = document.getElementById('unitSelect');
  var widthInput = document.getElementById('widthInput');
  var heightInput = document.getElementById('heightInput');
  var resizeBtn = document.getElementById('resizeBtn');

  var loadedImg = null;
  var currentDpi = 300;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  document.querySelectorAll('.dpi-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.dpi-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      currentDpi = parseInt(btn.getAttribute('data-dpi')) || 300;
    });
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

  resizeBtn.addEventListener('click', function () {
    if (!loadedImg) return;
    var unit = unitSelect.value;
    var wVal = parseFloat(widthInput.value) || 3.5;
    var hVal = parseFloat(heightInput.value) || 4.5;

    var pxW = 0, pxH = 0;
    if (unit === 'cm') {
      pxW = Math.round((wVal / 2.54) * currentDpi);
      pxH = Math.round((hVal / 2.54) * currentDpi);
    } else if (unit === 'mm') {
      pxW = Math.round((wVal / 25.4) * currentDpi);
      pxH = Math.round((hVal / 25.4) * currentDpi);
    } else {
      pxW = Math.round(wVal * currentDpi);
      pxH = Math.round(hVal * currentDpi);
    }

    var canvas = document.createElement('canvas');
    canvas.width = pxW;
    canvas.height = pxH;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(loadedImg, 0, 0, pxW, pxH);

    canvas.toBlob(function (blob) {
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'resized-' + wVal + unit + 'x' + hVal + unit + '.jpg';
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "resize-image-cm-mm.js"), "w", encoding="utf-8") as f:
    f.write(cm_js)

# 2. favicon-generator
fav_php = """<?php
$root = '../../';
$page_title = 'Favicon Generator Online Free — Create .ICO & Web Icons | Daily1Step';
$page_description = 'Generate favicon packages (16x16, 32x32, 48x48, 180x180 Apple Touch icon) from any logo image. 100% free and client-side.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Favicon Generator</h1>
      <p>Convert your PNG or JPG logo into multi-size website favicons and download ready-to-use icon package.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select logo image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <h4 style="margin:0 0 16px; font-size:.95rem; color:var(--ink);">Generated Icon Previews</h4>
        <div style="display:flex; justify-content:center; align-items:center; gap:20px; flex-wrap:wrap; margin-bottom:24px;">
          <div><canvas id="fav16" width="16" height="16" style="border:1px solid var(--border); width:32px; height:32px; image-rendering:pixelated; background:#fff;"></canvas><p style="font-size:.75rem; margin:4px 0 0;">16x16</p></div>
          <div><canvas id="fav32" width="32" height="32" style="border:1px solid var(--border); width:48px; height:48px; background:#fff;"></canvas><p style="font-size:.75rem; margin:4px 0 0;">32x32</p></div>
          <div><canvas id="fav48" width="48" height="48" style="border:1px solid var(--border); width:64px; height:64px; background:#fff;"></canvas><p style="font-size:.75rem; margin:4px 0 0;">48x48</p></div>
          <div><canvas id="fav180" width="180" height="180" style="border:1px solid var(--border); width:80px; height:80px; border-radius:12px; background:#fff;"></canvas><p style="font-size:.75rem; margin:4px 0 0;">180x180 (Apple)</p></div>
        </div>

        <button class="btn" id="downloadZipBtn">Download Favicon Package (.ZIP)</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/jszip.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/favicon-generator.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "favicon-generator"), exist_ok=True)
with open(os.path.join(tools_dir, "favicon-generator", "index.php"), "w", encoding="utf-8") as f:
    f.write(fav_php)

fav_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var downloadZipBtn = document.getElementById('downloadZipBtn');

  var f16 = document.getElementById('fav16');
  var f32 = document.getElementById('fav32');
  var f48 = document.getElementById('fav48');
  var f180 = document.getElementById('fav180');

  var loadedImg = null;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
        drawIcons();
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  function drawIcons() {
    [[f16, 16], [f32, 32], [f48, 48], [f180, 180]].forEach(function (pair) {
      var c = pair[0], s = pair[1];
      var ctx = c.getContext('2d');
      ctx.clearRect(0, 0, s, s);
      ctx.drawImage(loadedImg, 0, 0, s, s);
    });
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

  downloadZipBtn.addEventListener('click', function () {
    if (!loadedImg || typeof JSZip === 'undefined') return;
    var zip = new JSZip();
    var promises = [];

    var items = [
      { c: f16, name: 'favicon-16x16.png' },
      { c: f32, name: 'favicon-32x32.png' },
      { c: f48, name: 'favicon-48x48.png' },
      { c: f180, name: 'apple-touch-icon.png' }
    ];

    items.forEach(function (item) {
      promises.push(new Promise(function (resolve) {
        item.c.toBlob(function (blob) {
          zip.file(item.name, blob);
          resolve();
        }, 'image/png');
      }));
    });

    Promise.all(promises).then(function () {
      zip.generateAsync({ type: 'blob' }).then(function (zipBlob) {
        var url = URL.createObjectURL(zipBlob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'favicon-package.zip';
        a.click();
      });
    });
  });
})();
"""
with open(os.path.join(js_dir, "favicon-generator.js"), "w", encoding="utf-8") as f:
    f.write(fav_js)

# 3. join-images
join_php = """<?php
$root = '../../';
$page_title = 'Join Multiple Images Online Free — Merge Photos Horizontally / Vertically | Daily1Step';
$page_description = 'Combine and stitch multiple pictures into one single image horizontally or vertically. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Join Multiple Images</h1>
      <p>Stitch and combine multiple photos side-by-side (horizontally) or stacked (vertically).</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*" multiple>
      <p><strong>Click to select multiple images</strong> or drag and drop them here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:880px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <div style="display:flex; justify-content:center; gap:10px; margin-bottom:18px;">
          <button type="button" class="btn secondary active" id="joinHBtn">Side by Side (Horizontal)</button>
          <button type="button" class="btn secondary" id="joinVBtn">Stacked (Vertical)</button>
        </div>

        <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#fff; box-shadow:var(--shadow-sm);">
          <canvas id="previewCanvas" style="max-width:100%; max-height:420px; display:block;"></canvas>
        </div>

        <div style="margin-top:20px;">
          <button class="btn" id="downloadBtn">Download Combined Image</button>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/join-images.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "join-images"), exist_ok=True)
with open(os.path.join(tools_dir, "join-images", "index.php"), "w", encoding="utf-8") as f:
    f.write(join_php)

join_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var joinHBtn = document.getElementById('joinHBtn');
  var joinVBtn = document.getElementById('joinVBtn');
  var downloadBtn = document.getElementById('downloadBtn');

  var loadedImages = [];
  var isHorizontal = true;

  function loadFiles(files) {
    if (!files || files.length === 0) return;
    loadedImages = [];
    var count = files.length;
    var loadedCount = 0;

    Array.from(files).forEach(function (f) {
      var reader = new FileReader();
      reader.onload = function (e) {
        var img = new Image();
        img.onload = function () {
          loadedImages.push(img);
          loadedCount++;
          if (loadedCount === count) {
            dropzone.style.display = 'none';
            editorWrap.style.display = 'block';
            render();
          }
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(f);
    });
  }

  function render() {
    if (loadedImages.length === 0) return;
    if (isHorizontal) {
      var totalW = 0, maxH = 0;
      loadedImages.forEach(function (img) {
        totalW += img.naturalWidth || img.width;
        maxH = Math.max(maxH, img.naturalHeight || img.height);
      });
      canvas.width = totalW;
      canvas.height = maxH;
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, totalW, maxH);

      var curX = 0;
      loadedImages.forEach(function (img) {
        var w = img.naturalWidth || img.width;
        var h = img.naturalHeight || img.height;
        ctx.drawImage(img, curX, (maxH - h) / 2);
        curX += w;
      });
    } else {
      var maxW = 0, totalH = 0;
      loadedImages.forEach(function (img) {
        maxW = Math.max(maxW, img.naturalWidth || img.width);
        totalH += img.naturalHeight || img.height;
      });
      canvas.width = maxW;
      canvas.height = totalH;
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, maxW, totalH);

      var curY = 0;
      loadedImages.forEach(function (img) {
        var w = img.naturalWidth || img.width;
        var h = img.naturalHeight || img.height;
        ctx.drawImage(img, (maxW - w) / 2, curY);
        curY += h;
      });
    }
  }

  joinHBtn.addEventListener('click', function () { isHorizontal = true; joinHBtn.classList.add('active'); joinVBtn.classList.remove('active'); render(); });
  joinVBtn.addEventListener('click', function () { isHorizontal = false; joinVBtn.classList.add('active'); joinHBtn.classList.remove('active'); render(); });

  dropzone.addEventListener('click', function () { fileInput.click(); });
  fileInput.addEventListener('change', function (e) { loadFiles(e.target.files); fileInput.value = ''; });
  ['dragenter', 'dragover'].forEach(function (evt) {
    dropzone.addEventListener(evt, function (e) { e.preventDefault(); dropzone.classList.add('dragover'); });
  });
  ['dragleave', 'drop'].forEach(function (evt) {
    dropzone.addEventListener(evt, function (e) { e.preventDefault(); dropzone.classList.remove('dragover'); });
  });
  dropzone.addEventListener('drop', function (e) {
    if (e.dataTransfer && e.dataTransfer.files) loadFiles(e.dataTransfer.files);
  });

  downloadBtn.addEventListener('click', function () {
    canvas.toBlob(function (blob) {
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'joined-image.jpg';
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "join-images.js"), "w", encoding="utf-8") as f:
    f.write(join_js)

# 4. bulk-image-resizer
bulk_php = """<?php
$root = '../../';
$page_title = 'Bulk Image Resizer Online Free — Resize Multiple Photos to ZIP | Daily1Step';
$page_description = 'Resize multiple JPG, PNG, and WebP images at once in bulk and download all as a ZIP file. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Bulk Image Resizer</h1>
      <p>Resize dozens of photos simultaneously to fixed pixel dimensions or percentage and download as a ZIP.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*" multiple>
      <p><strong>Click to select multiple images</strong> or drag and drop them here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px;">
        <h4 style="margin:0 0 14px; font-size:.95rem; color:var(--ink);" id="fileCountText"></h4>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:14px; margin-bottom:18px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Target Max Width (px)</label>
            <input type="number" id="targetWidth" value="1200" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Target Max Height (px)</label>
            <input type="number" id="targetHeight" value="1200" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:700;">
          </div>
        </div>

        <button class="btn" id="bulkProcessBtn" style="width:100%;">Resize All & Download ZIP</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/jszip.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/bulk-image-resizer.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "bulk-image-resizer"), exist_ok=True)
with open(os.path.join(tools_dir, "bulk-image-resizer", "index.php"), "w", encoding="utf-8") as f:
    f.write(bulk_php)

bulk_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var fileCountText = document.getElementById('fileCountText');
  var targetWidth = document.getElementById('targetWidth');
  var targetHeight = document.getElementById('targetHeight');
  var bulkProcessBtn = document.getElementById('bulkProcessBtn');

  var selectedFiles = [];

  function loadFiles(files) {
    if (!files || files.length === 0) return;
    selectedFiles = Array.from(files);
    fileCountText.textContent = selectedFiles.length + ' Images Selected for Bulk Resizing';
    dropzone.style.display = 'none';
    editorWrap.style.display = 'block';
  }

  dropzone.addEventListener('click', function () { fileInput.click(); });
  fileInput.addEventListener('change', function (e) { loadFiles(e.target.files); fileInput.value = ''; });
  ['dragenter', 'dragover'].forEach(function (evt) {
    dropzone.addEventListener(evt, function (e) { e.preventDefault(); dropzone.classList.add('dragover'); });
  });
  ['dragleave', 'drop'].forEach(function (evt) {
    dropzone.addEventListener(evt, function (e) { e.preventDefault(); dropzone.classList.remove('dragover'); });
  });
  dropzone.addEventListener('drop', function (e) {
    if (e.dataTransfer && e.dataTransfer.files) loadFiles(e.dataTransfer.files);
  });

  bulkProcessBtn.addEventListener('click', function () {
    if (selectedFiles.length === 0 || typeof JSZip === 'undefined') return;
    bulkProcessBtn.disabled = true;
    bulkProcessBtn.textContent = 'Processing Images in Browser...';

    var maxW = parseInt(targetWidth.value) || 1200;
    var maxH = parseInt(targetHeight.value) || 1200;
    var zip = new JSZip();
    var promises = [];

    selectedFiles.forEach(function (file) {
      var p = new Promise(function (resolve) {
        var reader = new FileReader();
        reader.onload = function (e) {
          var img = new Image();
          img.onload = function () {
            var origW = img.naturalWidth || img.width;
            var origH = img.naturalHeight || img.height;
            var scale = Math.min(1, maxW / origW, maxH / origH);
            var drawW = Math.round(origW * scale);
            var drawH = Math.round(origH * scale);

            var canvas = document.createElement('canvas');
            canvas.width = drawW;
            canvas.height = drawH;
            var ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, drawW, drawH);

            canvas.toBlob(function (blob) {
              zip.file('resized_' + file.name, blob);
              resolve();
            }, 'image/jpeg', 0.90);
          };
          img.src = e.target.result;
        };
        reader.readAsDataURL(file);
      });
      promises.push(p);
    });

    Promise.all(promises).then(function () {
      zip.generateAsync({ type: 'blob' }).then(function (zipBlob) {
        var url = URL.createObjectURL(zipBlob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'bulk-resized-images.zip';
        a.click();
        bulkProcessBtn.disabled = false;
        bulkProcessBtn.textContent = 'Resize All & Download ZIP';
      });
    });
  });
})();
"""
with open(os.path.join(js_dir, "bulk-image-resizer.js"), "w", encoding="utf-8") as f:
    f.write(bulk_js)

# 5. add-border-image
border_php = """<?php
$root = '../../';
$page_title = 'Add Border to Photo Online Free — White & Custom Color Borders | Daily1Step';
$page_description = 'Add white, black, or custom colored borders and frames to photos for Instagram and profile avatars. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Add Border to Photo</h1>
      <p>Add stylish white, black, or custom color photo borders with adjustable thickness.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:880px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 300px; gap:20px; align-items:start;" class="border-grid">
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b;">
            <canvas id="previewCanvas" style="max-width:100%; max-height:420px; display:block;"></canvas>
          </div>
        </div>

        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:16px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Border Color</label>
            <input type="color" id="borderColor" value="#ffffff" style="width:100%; height:40px; border:1.5px solid var(--border); border-radius:8px; cursor:pointer;">
          </div>
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Border Thickness (% of photo)</label>
            <input type="range" id="borderThickness" min="2" max="25" value="6" style="width:100%;">
          </div>
          <button class="btn" id="downloadBtn" style="margin-top:8px;">Download Photo with Border</button>
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
  .border-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/add-border-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "add-border-image"), exist_ok=True)
with open(os.path.join(tools_dir, "add-border-image", "index.php"), "w", encoding="utf-8") as f:
    f.write(border_php)

border_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var borderColor = document.getElementById('borderColor');
  var borderThickness = document.getElementById('borderThickness');
  var downloadBtn = document.getElementById('downloadBtn');

  var loadedImg = null;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
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
    var origW = loadedImg.naturalWidth || loadedImg.width;
    var origH = loadedImg.naturalHeight || loadedImg.height;
    var borderPct = (parseInt(borderThickness.value) || 6) / 100;
    var bW = Math.round(Math.min(origW, origH) * borderPct);

    canvas.width = origW + bW * 2;
    canvas.height = origH + bW * 2;

    ctx.fillStyle = borderColor.value;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(loadedImg, bW, bW);
  }

  borderColor.addEventListener('input', render);
  borderThickness.addEventListener('input', render);

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
      a.download = 'photo-with-border.jpg';
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "add-border-image.js"), "w", encoding="utf-8") as f:
    f.write(border_js)

# 6. split-image
split_php = """<?php
$root = '../../';
$page_title = 'Split Image Online Free — Cut Image into Rows & Columns | Daily1Step';
$page_description = 'Cut and split any picture into custom rows and columns. Download all sliced parts in a ZIP archive. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Split Image into Pieces</h1>
      <p>Slice pictures into custom rows and columns grid and download pieces packaged in a ZIP archive.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select an image to split</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:880px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <div style="display:flex; justify-content:center; gap:16px; margin-bottom:18px;">
          <div>
            <label style="font-weight:700; font-size:.85rem; color:var(--ink);">Columns:</label>
            <input type="number" id="splitCols" value="2" min="1" max="10" style="width:70px; padding:6px; border:1.5px solid var(--border); border-radius:6px; font-weight:700;">
          </div>
          <div>
            <label style="font-weight:700; font-size:.85rem; color:var(--ink);">Rows:</label>
            <input type="number" id="splitRows" value="2" min="1" max="10" style="width:70px; padding:6px; border:1.5px solid var(--border); border-radius:6px; font-weight:700;">
          </div>
        </div>

        <div style="display:inline-block; max-width:100%; border:1.5px solid var(--border); border-radius:8px; overflow:hidden; background:#1e293b; box-shadow:var(--shadow-sm);">
          <canvas id="previewCanvas" style="max-width:100%; max-height:400px; display:block;"></canvas>
        </div>

        <div style="margin-top:20px;">
          <button class="btn" id="downloadZipBtn">Download Sliced Pieces (.ZIP)</button>
        </div>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/jszip.min.js"></script>
<script src="<?php echo $root; ?>assets/js/image-tools/split-image.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "split-image"), exist_ok=True)
with open(os.path.join(tools_dir, "split-image", "index.php"), "w", encoding="utf-8") as f:
    f.write(split_php)

split_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var canvas = document.getElementById('previewCanvas');
  var ctx = canvas.getContext('2d');
  var splitCols = document.getElementById('splitCols');
  var splitRows = document.getElementById('splitRows');
  var downloadZipBtn = document.getElementById('downloadZipBtn');

  var loadedImg = null;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
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
    var w = loadedImg.naturalWidth || loadedImg.width;
    var h = loadedImg.naturalHeight || loadedImg.height;
    canvas.width = w;
    canvas.height = h;
    ctx.drawImage(loadedImg, 0, 0, w, h);

    var cols = parseInt(splitCols.value) || 2;
    var rows = parseInt(splitRows.value) || 2;
    var tW = w / cols, tH = h / rows;

    ctx.strokeStyle = '#e5322d';
    ctx.lineWidth = Math.max(2, Math.round(w * 0.003));
    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        ctx.strokeRect(c * tW, r * tH, tW, tH);
      }
    }
  }

  splitCols.addEventListener('input', render);
  splitRows.addEventListener('input', render);

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

  downloadZipBtn.addEventListener('click', function () {
    if (!loadedImg || typeof JSZip === 'undefined') return;
    var zip = new JSZip();
    var cols = parseInt(splitCols.value) || 2;
    var rows = parseInt(splitRows.value) || 2;

    var fullW = loadedImg.naturalWidth || loadedImg.width;
    var fullH = loadedImg.naturalHeight || loadedImg.height;
    var tileW = Math.floor(fullW / cols);
    var tileH = Math.floor(fullH / rows);

    var tileCanvas = document.createElement('canvas');
    tileCanvas.width = tileW;
    tileCanvas.height = tileH;
    var tCtx = tileCanvas.getContext('2d');

    var promises = [];
    var pieceNum = 1;

    for (var r = 0; r < rows; r++) {
      for (var c = 0; c < cols; c++) {
        (function (row, col, idx) {
          tCtx.clearRect(0, 0, tileW, tileH);
          tCtx.drawImage(loadedImg, col * tileW, row * tileH, tileW, tileH, 0, 0, tileW, tileH);
          var p = new Promise(function (resolve) {
            tileCanvas.toBlob(function (blob) {
              zip.file('piece_' + idx + '.jpg', blob);
              resolve();
            }, 'image/jpeg', 0.95);
          });
          promises.push(p);
          pieceNum++;
        })(r, c, pieceNum);
      }
    }

    Promise.all(promises).then(function () {
      zip.generateAsync({ type: 'blob' }).then(function (zipBlob) {
        var url = URL.createObjectURL(zipBlob);
        var a = document.createElement('a');
        a.href = url;
        a.download = 'split-image-pieces.zip';
        a.click();
      });
    });
  });
})();
"""
with open(os.path.join(js_dir, "split-image.js"), "w", encoding="utf-8") as f:
    f.write(split_js)

# 7. exif-metadata-remover
exif_php = """<?php
$root = '../../';
$page_title = 'Remove EXIF Metadata Online Free — Strip GPS & Camera Data | Daily1Step';
$page_description = 'Strip GPS location data, camera information, timestamp, and device metadata from JPG/PNG photos for privacy before sharing. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Remove EXIF & GPS Metadata</h1>
      <p>Clean location coordinates, camera models, dates, and device tags to protect your online privacy.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select a photo to clean</strong> or drag and drop it here</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:820px; margin:20px auto 0;">
      <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:22px; text-align:center;">
        <h4 style="margin:0 0 8px; font-size:1.1rem; color:var(--ink);" id="fileName"></h4>
        <p style="color:var(--ink-soft); font-size:.88rem; margin-bottom:18px;">Photo will be re-encoded on clean canvas with all EXIF headers stripped.</p>

        <button class="btn" id="cleanBtn">Strip Metadata & Download</button>
      </div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/exif-metadata-remover.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
os.makedirs(os.path.join(tools_dir, "exif-metadata-remover"), exist_ok=True)
with open(os.path.join(tools_dir, "exif-metadata-remover", "index.php"), "w", encoding="utf-8") as f:
    f.write(exif_php)

exif_js = """(function () {
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var editorWrap = document.getElementById('editorWrap');
  var fileNameEl = document.getElementById('fileName');
  var cleanBtn = document.getElementById('cleanBtn');

  var loadedImg = null;
  var currentFile = null;

  function loadFile(file) {
    if (!file || !file.type.match(/image.*/)) return;
    currentFile = file;
    fileNameEl.textContent = file.name;
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        loadedImg = img;
        dropzone.style.display = 'none';
        editorWrap.style.display = 'block';
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
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

  cleanBtn.addEventListener('click', function () {
    if (!loadedImg) return;
    var canvas = document.createElement('canvas');
    canvas.width = loadedImg.naturalWidth || loadedImg.width;
    canvas.height = loadedImg.naturalHeight || loadedImg.height;
    var ctx = canvas.getContext('2d');
    ctx.drawImage(loadedImg, 0, 0);

    canvas.toBlob(function (blob) {
      var url = URL.createObjectURL(blob);
      var a = document.createElement('a');
      a.href = url;
      a.download = 'cleaned_' + currentFile.name;
      a.click();
    }, 'image/jpeg', 0.95);
  });
})();
"""
with open(os.path.join(js_dir, "exif-metadata-remover.js"), "w", encoding="utf-8") as f:
    f.write(exif_js)

print("Remaining special tools generation complete.")
