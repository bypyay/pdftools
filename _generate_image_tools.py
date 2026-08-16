import os

base_dir = r"D:\Codding\Claude Cowork code\PDF Tools"
tools_dir = os.path.join(base_dir, "image-tools")
js_dir = os.path.join(base_dir, "assets", "js", "image-tools")

os.makedirs(tools_dir, exist_ok=True)
os.makedirs(js_dir, exist_ok=True)

image_tools_meta = [
    {
        "slug": "png-to-jpg",
        "title": "PNG to JPG Converter Online Free",
        "h1": "PNG to JPG Converter",
        "desc": "Convert PNG images to JPG with white background fill and quality slider.",
        "accept": "image/png",
        "out_ext": "jpg",
        "out_mime": "image/jpeg"
    },
    {
        "slug": "jpg-to-png",
        "title": "JPG to PNG Converter Online Free",
        "h1": "JPG to PNG Converter",
        "desc": "Convert JPG pictures to lossless PNG format instantly in your browser.",
        "accept": "image/jpeg",
        "out_ext": "png",
        "out_mime": "image/png"
    },
    {
        "slug": "webp-to-jpg",
        "title": "WEBP to JPG Converter Online Free",
        "h1": "WEBP to JPG Converter",
        "desc": "Convert modern WebP images to universal JPG format online.",
        "accept": "image/webp",
        "out_ext": "jpg",
        "out_mime": "image/jpeg"
    },
    {
        "slug": "image-to-jpg",
        "title": "Image to JPG Converter Online Free",
        "h1": "Image to JPG Converter",
        "desc": "Convert any image (PNG, WEBP, GIF, SVG, BMP) to high quality JPG format.",
        "accept": "image/*",
        "out_ext": "jpg",
        "out_mime": "image/jpeg"
    },
    {
        "slug": "grayscale-image",
        "title": "Black and White Image Converter Online Free",
        "h1": "Grayscale & Black/White Image",
        "desc": "Convert full color photos to aesthetic Black & White or Monochrome tone.",
        "accept": "image/*",
        "out_ext": "jpg",
        "out_mime": "image/jpeg"
    }
]

for t in image_tools_meta:
    tool_folder = os.path.join(tools_dir, t["slug"])
    os.makedirs(tool_folder, exist_ok=True)
    
    # PHP index.php
    php_content = f"""<?php
$root = '../../';
$page_title = '{t["title"]} | Daily1Step';
$page_description = '{t["desc"]} 100% free and private.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>{t["h1"]}</h1>
      <p>{t["desc"]}</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="{t["accept"]}">
      <p><strong>Click to select an image</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Fast and 100% private in browser</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:820px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="fileSize"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="display:flex; justify-content:center; margin:20px 0;">
        <img id="imgPreview" style="max-width:300px; max-height:240px; border-radius:8px; border:1.5px solid var(--border); background:#fff; object-fit:contain;">
      </div>

      <div class="actions" id="actions">
        <button class="btn" id="convertBtn">Convert Image</button>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Image Processed Successfully!</h3>
      <div style="display:flex; justify-content:center; margin:16px 0;">
        <img id="finalImg" style="max-width:300px; max-height:240px; border-radius:8px; border:1.5px solid var(--border); box-shadow:var(--shadow);">
      </div>
      <a class="btn" id="downloadLink" download="converted.{t['out_ext']}">Download {t['out_ext'].upper()} Image</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Process another image</button></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<script src="<?php echo $root; ?>assets/js/image-tools/{t['slug']}.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
"""
    with open(os.path.join(tool_folder, "index.php"), "w", encoding="utf-8") as f:
        f.write(php_content)

    # JS file
    is_grayscale = (t["slug"] == "grayscale-image")
    js_content = f"""(function () {{
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var fileInfo = document.getElementById('fileInfo');
  var fileNameEl = document.getElementById('fileName');
  var fileSizeEl = document.getElementById('fileSize');
  var removeFileBtn = document.getElementById('removeFile');
  var imgPreview = document.getElementById('imgPreview');
  var convertBtn = document.getElementById('convertBtn');
  var resultBox = document.getElementById('resultBox');
  var finalImg = document.getElementById('finalImg');
  var downloadLink = document.getElementById('downloadLink');
  var resetBtn = document.getElementById('resetBtn');

  var loadedImg = null;
  var currentFile = null;

  function formatSize(bytes) {{
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
  }}

  function loadFile(file) {{
    if (!file) return;
    currentFile = file;
    fileNameEl.textContent = file.name;
    fileSizeEl.textContent = formatSize(file.size);

    var reader = new FileReader();
    reader.onload = function (e) {{
      var img = new Image();
      img.onload = function () {{
        loadedImg = img;
        imgPreview.src = e.target.result;
        dropzone.style.display = 'none';
        fileInfo.style.display = 'block';
      }};
      img.src = e.target.result;
    }};
    reader.readAsDataURL(file);
  }}

  dropzone.addEventListener('click', function () {{ fileInput.click(); }});
  fileInput.addEventListener('change', function (e) {{ loadFile(e.target.files[0]); fileInput.value = ''; }});
  ['dragenter', 'dragover'].forEach(function (evt) {{
    dropzone.addEventListener(evt, function (e) {{ e.preventDefault(); dropzone.classList.add('dragover'); }});
  }});
  ['dragleave', 'drop'].forEach(function (evt) {{
    dropzone.addEventListener(evt, function (e) {{ e.preventDefault(); dropzone.classList.remove('dragover'); }});
  }});
  dropzone.addEventListener('drop', function (e) {{
    if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0]) loadFile(e.dataTransfer.files[0]);
  }});

  removeFileBtn.addEventListener('click', function () {{
    loadedImg = null;
    dropzone.style.display = 'block';
    fileInfo.style.display = 'none';
  }});

  convertBtn.addEventListener('click', function () {{
    if (!loadedImg) return;
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    var w = loadedImg.naturalWidth || loadedImg.width;
    var h = loadedImg.naturalHeight || loadedImg.height;
    canvas.width = w;
    canvas.height = h;

    {"ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, w, h);" if t["out_ext"] == "jpg" else ""}
    ctx.drawImage(loadedImg, 0, 0, w, h);

    {'''
    // Grayscale filter
    var imgData = ctx.getImageData(0, 0, w, h);
    var d = imgData.data;
    for (var i = 0; i < d.length; i += 4) {
      var avg = (d[i] * 0.299 + d[i + 1] * 0.587 + d[i + 2] * 0.114);
      d[i] = avg; d[i + 1] = avg; d[i + 2] = avg;
    }
    ctx.putImageData(imgData, 0, 0);
    ''' if is_grayscale else ''}

    canvas.toBlob(function (blob) {{
      var url = URL.createObjectURL(blob);
      finalImg.src = url;
      downloadLink.href = url;
      var outName = currentFile.name.replace(/\.[^/.]+$/, '') + '-converted.{t["out_ext"]}';
      downloadLink.download = outName;
      downloadLink.textContent = 'Download ' + outName;

      fileInfo.style.display = 'none';
      resultBox.style.display = 'block';
    }}, '{t["out_mime"]}', 0.95);
  }});

  resetBtn.addEventListener('click', function () {{
    loadedImg = null;
    dropzone.style.display = 'block';
    fileInfo.style.display = 'none';
    resultBox.style.display = 'none';
  }});
}})();
"""
    with open(os.path.join(js_dir, f"{t['slug']}.js"), "w", encoding="utf-8") as f:
        f.write(js_content)

print("Standard converter batch completed successfully.")
