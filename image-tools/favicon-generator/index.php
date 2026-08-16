<?php
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
