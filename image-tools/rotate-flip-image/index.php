<?php
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
