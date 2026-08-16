<?php
$root = '../../';
$page_title = 'Sign PDF Online Free — eSign PDF Documents | Daily1Step PDF';
$page_description = 'Sign PDF documents online for free. Draw your signature, type your name, or upload a signature image. Drag & drop signature on any page. Processed entirely in your browser.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Sign PDF</h1>
      <p>Draw, type, or upload your signature and place it anywhere on your PDF document.</p>
    </div>

    <div class="handoff-banner" id="handoffBanner">
      <span>&#10003;</span> <span id="handoffBannerText"></span>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="application/pdf">
      <p><strong>Click to select a PDF file</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">One file at a time</p>
    </div>

    <div id="fileInfo" style="display:none; max-width:980px; margin:20px auto 0;">
      <div class="file-row">
        <span class="name" id="fileName"></span>
        <span class="size" id="pageCount"></span>
        <button class="remove" id="removeFile" title="Remove">&times;</button>
      </div>

      <div style="display:flex; gap:28px; flex-wrap:wrap; margin-top:24px;">
        <!-- Left: Signature Creator -->
        <div style="flex:1.1; min-width:300px;">
          <div style="border-bottom:2px solid var(--border); padding-bottom:8px; margin-bottom:16px; display:flex; gap:8px;">
            <button type="button" class="wm-tab-btn active" id="tabDrawBtn" style="flex:1; padding:9px 12px; border:none; border-radius:8px; font-weight:700; font-size:.9rem; cursor:pointer; background:var(--red); color:#fff;">✍️ Draw</button>
            <button type="button" class="wm-tab-btn" id="tabTypeBtn" style="flex:1; padding:9px 12px; border:1px solid var(--border); border-radius:8px; font-weight:700; font-size:.9rem; cursor:pointer; background:var(--bg-soft); color:var(--ink);">⌨️ Type</button>
            <button type="button" class="wm-tab-btn" id="tabUploadBtn" style="flex:1; padding:9px 12px; border:1px solid var(--border); border-radius:8px; font-weight:700; font-size:.9rem; cursor:pointer; background:var(--bg-soft); color:var(--ink);">📁 Upload</button>
          </div>

          <!-- Draw Pad -->
          <div id="drawSection">
            <div style="border:2px solid var(--border); border-radius:10px; background:#fff; overflow:hidden; position:relative;">
              <canvas id="sigPad" width="360" height="140" style="display:block; width:100%; height:140px; cursor:crosshair; background:#fff; touch-action:none;"></canvas>
              <button type="button" id="clearPadBtn" style="position:absolute; bottom:6px; right:6px; background:var(--bg-soft); border:1px solid var(--border); border-radius:6px; padding:3px 8px; font-size:.75rem; font-weight:600; cursor:pointer;">Clear</button>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:8px;">
              <div style="display:flex; gap:6px; align-items:center;">
                <label style="font-size:.8rem; font-weight:600;">Ink Color:</label>
                <input type="color" id="inkColor" value="#000000" style="width:36px; height:26px; border:1px solid var(--border); border-radius:4px; cursor:pointer; padding:1px;">
              </div>
              <span style="font-size:.78rem; color:var(--ink-soft);">Draw inside the box</span>
            </div>
          </div>

          <!-- Type Signature -->
          <div id="typeSection" style="display:none;">
            <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Type your name</label>
            <input type="text" id="typeSigInput" placeholder="e.g. John Doe" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-size:1.1rem; margin-bottom:10px;">
            <div id="typedPreview" style="padding:14px; background:#fff; border:1.5px solid var(--border); border-radius:8px; font-family:'Brush Script MT', cursive, sans-serif; font-size:1.8rem; text-align:center; color:#000; min-height:56px;">John Doe</div>
          </div>

          <!-- Upload Signature -->
          <div id="uploadSection" style="display:none;">
            <div id="sigUploadDropzone" style="border:2px dashed var(--border); border-radius:10px; padding:20px; text-align:center; cursor:pointer; background:var(--bg-soft);">
              <input type="file" id="sigFileInput" accept="image/png, image/jpeg, image/webp" style="display:none;">
              <p style="margin:0; font-weight:600; font-size:.9rem;">Click to upload signature image</p>
              <p style="margin:4px 0 0; font-size:.78rem; color:var(--ink-soft);">PNG with transparent background recommended</p>
            </div>
          </div>

          <!-- Signature Controls -->
          <div style="margin-top:16px; padding-top:16px; border-top:1px solid var(--border);">
            <div style="margin-bottom:12px;">
              <label style="display:block; font-weight:600; font-size:.85rem; margin-bottom:4px;">Signature Size: <span id="sigScaleVal" style="font-weight:700; color:var(--red);">60%</span></label>
              <input type="range" id="sigScale" min="20" max="150" value="60" style="width:100%; accent-color:var(--red);">
            </div>

            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
              <label style="font-size:.85rem; font-weight:600;">Sign on page:</label>
              <select id="pageSelect" style="padding:6px 12px; border:1.5px solid var(--border); border-radius:6px; font-weight:600;"></select>
            </div>

            <label style="display:flex; align-items:center; gap:8px; font-size:.85rem; font-weight:600; cursor:pointer; margin-bottom:6px;">
              <input type="checkbox" id="addDateCheck"> Add Date Stamp (Today: <?php echo date('d/m/Y'); ?>)
            </label>
          </div>
        </div>

        <!-- Right: Interactive Page Preview -->
        <div style="flex:1.2; min-width:300px; text-align:center;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
            <label style="font-weight:700; font-size:.9rem; color:var(--ink);">Live Document Preview</label>
            <span style="font-size:.78rem; color:var(--red); font-weight:600;">✨ Drag signature to place</span>
          </div>

          <div id="sigCanvasContainer" style="position:relative; display:inline-block; border:2px solid var(--border); border-radius:12px; overflow:hidden; background:#fff; box-shadow:var(--shadow-sm); user-select:none;">
            <div id="sigPreviewWrap"></div>
          </div>
          <p style="color:var(--ink-soft); font-size:.8rem; margin:10px auto 0;">Click and drag signature on the page to adjust placement.</p>
        </div>
      </div>
    </div>

    <div class="actions" id="actions" style="display:none;">
      <button class="btn" id="signBtn">Sign &amp; Download PDF</button>
    </div>

    <div class="progress-wrap" id="progressWrap">
      <div class="progress-bar"><div id="progressBar"></div></div>
      <div class="status-text" id="statusText">Applying signature...</div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Your signed PDF is ready</h3>
      <p id="resultInfo"></p>
      <a class="btn" id="downloadLink" download="signed.pdf">Download signed.pdf</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Sign another file</button></div>
    </div>

    <div class="continue-box" id="continueBox" style="display:none;">
      <p class="continue-title">Continue to&hellip;</p>
      <div class="continue-grid" id="continueGrid"></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your files and signatures never leave your device — signed 100% locally in your browser.
    </p>

    <section class="info-section">
      <h2>How to sign a PDF document</h2>
      <ol>
        <li>Upload your PDF file.</li>
        <li>Create your signature by <strong>Drawing</strong> with your finger/mouse, <strong>Typing</strong>, or <strong>Uploading an image</strong>.</li>
        <li>Drag and place your signature exactly where you want it on the document preview.</li>
        <li>Click <strong>Sign &amp; Download PDF</strong>.</li>
      </ol>
    </section>
  </div>
</section>

<script src="<?php echo $root; ?>vendor/pdf-lib.min.js"></script>
<script src="<?php echo $root; ?>vendor/pdf.min.js"></script>
<script src="<?php echo $root; ?>assets/js/handoff.js"></script>
<script src="<?php echo $root; ?>assets/js/tools/sign-pdf.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
