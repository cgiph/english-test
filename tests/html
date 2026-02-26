<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>English Test | Practice & Assessment</title>
  <meta name="description" content="An interactive English test for grammar, vocabulary, and reading comprehension."/>
  <link rel="icon" href="favicon.png" />
  <link rel="preload" href="styles.css" as="style" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="site-header" role="banner">
    <h1 id="app-title">English Test</h1>
    <p class="subtitle">Grammar • Vocabulary • Reading</p>
  </header>

  <main id="app" class="container" role="main" aria-labelledby="app-title">
    <!-- Settings / Start -->
    <section id="start-screen" class="card">
      <h2>Get Started</h2>

      <form id="start-form" novalidate>
        <div class="field">
          <label for="testeeName">Your Name</label>
          <input id="testeeName" name="testeeName" type="text" placeholder="e.g., Maria S. Centino" autocomplete="name" />
        </div>

        <div class="field">
          <label for="mode">Feedback Mode</label>
          <select id="mode" name="mode" aria-describedby="modeHelp">
            <option value="end">Show feedback at the end (recommended)</option>
            <option value="instant">Show feedback after each question</option>
          </select>
          <small id="modeHelp" class="help">Choose how you want feedback to appear.</small>
        </div>

        <div class="field grid-2">
          <div>
            <label for="category">Category</label>
            <select id="category" name="category">
              <option value="all">All</option>
              <option value="grammar">Grammar</option>
              <option value="vocabulary">Vocabulary</option>
              <option value="reading">Reading</option>
            </select>
          </div>
          <div>
            <label for="limit">Number of Questions</label>
            <input id="limit" name="limit" type="number" min="3" max="30" step="1" value="10" />
          </div>
        </div>

        <div class="field grid-2">
          <div>
            <label for="duration">Time Limit (minutes)</label>
            <input id="duration" name="duration" type="number" min="0" max="120" step="1" value="15" />
            <small class="help">Set 0 for no timer.</small>
          </div>
          <div class="checkbox">
            <input id="shuffle" name="shuffle" type="checkbox" checked />
            <label for="shuffle">Shuffle questions</label>
          </div>
        </div>

        <button type="submit" class="btn primary" id="startBtn">Start Test</button>
      </form>
    </section>

    <!-- Test UI -->
    <section id="test-screen" class="card hidden" aria-live="polite">
      <div class="test-header">
        <div class="status">
          <span id="progressText" aria-live="polite">Question 1 of N</span>
          <div class="progress" aria-label="Progress">
            <div id="progressBar" class="progress-bar" style="width: 0%;"></div>
          </div>
        </div>
        <div class="timer" id="timer" aria-live="polite" aria-atomic="true">⏱ 00:00</div>
      </div>

      <div id="questionContainer" class="question-container" role="group" aria-labelledby="questionPrompt">
        <!-- Filled by script -->
      </div>

      <div class="controls">
        <button class="btn" id="prevBtn" type="button" aria-label="Previous question">◀ Prev</button>
        <button class="btn" id="nextBtn" type="button" aria-label="Next question">Next ▶</button>
        <button class="btn ghost" id="flagBtn" type="button" aria-pressed="false">🚩 Flag</button>
        <button class="btn danger" id="finishBtn" type="button">Finish</button>
      </div>
    </section>

    <!-- Results -->
    <section id="result-screen" class="card hidden">
      <h2>Results</h2>
      <div class="result-summary">
        <p><strong>Name:</strong> <span id="resName">—</span></p>
        <p><strong>Score:</strong> <span id="resScore">0</span>/<span id="resTotal">0</span> (<span id="resPercent">0%</span>)</p>
        <p><strong>Time:</strong> <span id="resTime">—</span></p>
      </div>

      <div class="result-actions">
        <button class="btn primary" id="reviewBtn" type="button">Review Answers</button>
        <button class="btn" id="retryBtn" type="button">Try Again</button>
        <button class="btn ghost" id="exportBtn" type="button">Export CSV</button>
        <button class="btn ghost" id="printBtn" type="button">Print</button>
      </div>

      <div id="reviewContainer" class="review-container hidden" aria-live="polite">
        <!-- Filled by script -->
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <p>© <span id="year"></span> English Test • Built for educators and learners.</p>
  </footer>

  <script src="questions.js"></script>
  <script src="script.js"></script>
</body>
</html>
``
