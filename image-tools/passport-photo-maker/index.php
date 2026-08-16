<?php
$root = '../../';
$page_title = 'Passport Size Photo Maker Online Free — 3.5x4.5cm, 2x2 Inch, Print Sheet | Daily1Step';
$page_description = 'Create passport and visa size photos online (3.5x4.5 cm, 35x45 mm, 2x2 inch). Change background to white/blue, crop face, and generate 4x6 / A4 printable photo sheets. 100% free.';
include __DIR__ . '/../../includes/header.php';
?>
<section class="tool-page">
  <div class="container">
    <div class="tool-header">
      <h1>Passport Size Photo Maker</h1>
      <p>Create professional passport & visa photos with custom background colors and printable multi-photo sheets.</p>
    </div>

    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="image/*">
      <p><strong>Click to select a photo</strong> or drag and drop it here</p>
      <p style="color:var(--ink-soft); font-size:.85rem;">Works best with clear portrait photos</p>
    </div>

    <div id="editorWrap" style="display:none; max-width:960px; margin:20px auto 0;">
      <div style="display:grid; grid-template-columns:1fr 340px; gap:24px; align-items:start;" class="passport-grid">
        <!-- Canvas Preview -->
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; text-align:center;">
          <h4 style="margin:0 0 12px; font-size:.95rem; color:var(--ink);">Interactive Photo Preview & Alignment</h4>
          <div style="position:relative; display:inline-block; max-width:100%; border:2px dashed #cbd5e1; border-radius:8px; overflow:hidden; background:#e2e8f0;">
            <canvas id="passportCanvas" style="max-width:100%; max-height:420px; display:block; cursor:move;"></canvas>
            <div id="cropOverlay" style="position:absolute; pointer-events:none; border:2px solid var(--red); box-shadow:0 0 0 9999px rgba(0,0,0,0.45); top:0; left:0; width:100%; height:100%;">
              <!-- Face Oval Guide -->
              <div style="position:absolute; top:15%; left:25%; width:50%; height:60%; border:1.5px dashed rgba(255,255,255,0.8); border-radius:50%;"></div>
            </div>
          </div>
          <p style="font-size:.78rem; color:var(--ink-soft); margin:8px 0 0;">Drag photo to position head inside oval guide. Use slider to zoom.</p>
        </div>

        <!-- Controls -->
        <div style="background:var(--bg-soft); border:1.5px solid var(--border); border-radius:14px; padding:20px; display:flex; flex-direction:column; gap:16px;">
          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Country & Size Preset</label>
            <select id="presetSelect" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:600;">
              <option value="35x45">India / Standard (3.5 cm x 4.5 cm)</option>
              <option value="35x45_mm">Schengen / UK / Europe (35 mm x 45 mm)</option>
              <option value="51x51">USA Visa / Passport (2 x 2 Inch / 51x51 mm)</option>
              <option value="35x35">3.5 cm x 3.5 cm</option>
              <option value="custom">Custom Dimensions</option>
            </select>
          </div>

          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Photo Background Color</label>
            <div style="display:flex; gap:8px;">
              <button type="button" class="bg-btn active" data-bg="original" style="flex:1;">Original</button>
              <button type="button" class="bg-btn" data-bg="#ffffff" style="flex:1; border-color:#cbd5e1; background:#fff; color:#18191f;">White</button>
              <button type="button" class="bg-btn" data-bg="#d0e3ff" style="flex:1; background:#d0e3ff; color:#1e40af;">Blue</button>
              <button type="button" class="bg-btn" data-bg="#fee2e2" style="flex:1; background:#fee2e2; color:#991b1b;">Red</button>
            </div>
          </div>

          <div>
            <div style="display:flex; justify-content:space-between; font-weight:700; font-size:.85rem; margin-bottom:4px;">
              <span>Zoom / Scale</span>
              <span id="zoomVal">100%</span>
            </div>
            <input type="range" id="zoomRange" min="50" max="250" value="100" style="width:100%;">
          </div>

          <div>
            <label style="display:block; font-weight:700; font-size:.88rem; margin-bottom:6px; color:var(--ink);">Output Format</label>
            <select id="outputMode" style="width:100%; padding:10px; border:1.5px solid var(--border); border-radius:8px; font-weight:600;">
              <option value="single">Single Photo (.jpg)</option>
              <option value="sheet_4x6_6">Print Sheet: 4x6 Inch (6 Photos)</option>
              <option value="sheet_a4_8">Print Sheet: A4 Paper (8 Photos)</option>
            </select>
          </div>

          <button class="btn" id="generateBtn" style="margin-top:8px;">Generate Passport Photo</button>
        </div>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Passport Photo Ready!</h3>
      <p id="resultInfo">Your passport photo is processed with official specifications.</p>
      <div style="display:flex; justify-content:center; margin:14px 0;">
        <img id="finalImg" style="max-width:320px; max-height:260px; border-radius:8px; border:1.5px solid var(--border); box-shadow:var(--shadow);">
      </div>
      <a class="btn" id="downloadLink" download="passport-photo.jpg">Download Photo</a>
      <div style="margin-top:12px;"><button class="btn secondary" id="resetBtn">Make another photo</button></div>
    </div>

    <p class="privacy-note">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
      Your photos never leave your device — processed 100% locally in your browser.
    </p>
  </div>
</section>

<style>
.bg-btn {
  padding: 8px 10px;
  border-radius: 8px;
  border: 1.5px solid var(--border);
  font-weight: 700;
  font-size: .8rem;
  cursor: pointer;
  transition: all .15s;
}
.bg-btn.active {
  border-color: var(--red);
  box-shadow: 0 0 0 2px var(--red-glow);
}
@media (max-width: 768px) {
  .passport-grid { grid-template-columns: 1fr !important; }
}
</style>

<script src="<?php echo $root; ?>assets/js/image-tools/passport-photo-maker.js"></script>
<?php include __DIR__ . '/../../includes/footer.php'; ?>
