"""
TaskFlow Architecture Documentation PDF Generator
Generates a comprehensive LaTeX-styled PDF using fpdf2.
"""

from fpdf import FPDF
import datetime


class TaskFlowDoc(FPDF):
    INDIGO = (99, 102, 241)
    INDIGO_DARK = (79, 70, 229)
    DARK_BG = (15, 23, 42)
    GRAY_700 = (51, 65, 85)
    GRAY_500 = (100, 116, 139)
    GRAY_400 = (148, 163, 184)
    GRAY_200 = (226, 232, 240)
    WHITE = (255, 255, 255)
    SUCCESS = (16, 185, 129)
    WARNING = (245, 158, 11)
    DANGER = (239, 68, 68)
    ACCENT = (6, 182, 212)
    CODE_BG = (241, 245, 249)

    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*self.GRAY_500)
        self.cell(0, 8, "TaskFlow - Architecture Documentation", align="L")
        self.cell(0, 8, f"Page {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.GRAY_200)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(6)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*self.GRAY_400)
        self.cell(0, 10, f"Generated {datetime.date.today().strftime('%B %d, %Y')}  |  TaskFlow v2.0", align="C")

    # ---- Reusable helpers ----

    def cover_page(self):
        self.add_page()
        # Big gradient-like header block
        self.set_fill_color(*self.INDIGO)
        self.rect(0, 0, 210, 120, "F")
        self.set_fill_color(*self.INDIGO_DARK)
        self.rect(0, 100, 210, 20, "F")

        self.set_y(32)
        self.set_font("Helvetica", "B", 42)
        self.set_text_color(*self.WHITE)
        self.cell(0, 16, "TaskFlow", align="C", new_x="LMARGIN", new_y="NEXT")

        self.set_font("Helvetica", "", 14)
        self.set_text_color(200, 200, 255)
        self.cell(0, 10, "Smart Todo Manager", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(6)
        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Architecture & Developer Documentation", align="C", new_x="LMARGIN", new_y="NEXT")

        # Subtitle box
        self.set_y(135)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(*self.GRAY_700)
        self.cell(0, 8, "Version 2.0  |  February 2026", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(*self.GRAY_500)
        self.cell(0, 8, "A complete guide to understanding, maintaining, and extending the TaskFlow application.", align="C", new_x="LMARGIN", new_y="NEXT")

        # Tech badges
        self.ln(10)
        techs = ["HTML5", "CSS3", "JavaScript ES6+", "Chart.js", "LocalStorage API"]
        total_w = sum(self.get_string_width(t) + 14 for t in techs) + 6 * (len(techs) - 1)
        start_x = (210 - total_w) / 2
        self.set_x(start_x)
        for t in techs:
            w = self.get_string_width(t) + 14
            self.set_fill_color(*self.INDIGO)
            self.set_text_color(*self.WHITE)
            self.set_font("Helvetica", "B", 9)
            self.cell(w, 22, t, align="C", fill=True)
            self.set_x(self.get_x() + 6)

    def section_title(self, number, title):
        self.ln(6)
        self.set_font("Helvetica", "B", 20)
        self.set_text_color(*self.INDIGO)
        self.cell(0, 12, f"{number}. {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*self.INDIGO)
        self.set_line_width(0.6)
        self.line(self.l_margin, self.get_y() + 1, self.l_margin + 60, self.get_y() + 1)
        self.set_line_width(0.2)
        self.ln(6)

    def subsection(self, title):
        self.ln(3)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*self.GRAY_700)
        self.cell(0, 9, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def subsubsection(self, title):
        self.ln(2)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*self.GRAY_700)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def body_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*self.GRAY_700)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bullet(self, text, level=0):
        indent = 10 + level * 8
        self.set_x(self.l_margin + indent)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*self.INDIGO)
        marker = ">" if level == 0 else "-"
        self.cell(6, 5.5, marker)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*self.GRAY_700)
        remaining_w = self.w - self.get_x() - self.r_margin
        self.multi_cell(remaining_w, 5.5, text)
        self.ln(1)

    def code_block(self, code, title=None):
        if title:
            self.set_font("Helvetica", "B", 8)
            self.set_text_color(*self.GRAY_500)
            self.cell(0, 5, title, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)
        self.set_fill_color(*self.CODE_BG)
        self.set_draw_color(*self.GRAY_200)
        x = self.l_margin
        w = self.w - self.l_margin - self.r_margin
        self.set_font("Courier", "", 8)
        self.set_text_color(*self.GRAY_700)
        lines = code.strip().split("\n")
        line_h = 4.2
        block_h = len(lines) * line_h + 8
        if self.get_y() + block_h > self.h - self.b_margin:
            self.add_page()
        y_start = self.get_y()
        self.rect(x, y_start, w, block_h, "FD")
        self.set_y(y_start + 4)
        for line in lines:
            self.set_x(x + 6)
            self.cell(w - 12, line_h, line[:120], new_x="LMARGIN", new_y="NEXT")
        self.set_y(y_start + block_h + 2)
        self.ln(2)

    def info_box(self, text, color=None):
        if color is None:
            color = self.INDIGO
        x = self.l_margin
        w = self.w - self.l_margin - self.r_margin
        self.set_fill_color(color[0], color[1], color[2])
        self.rect(x, self.get_y(), 3, 18, "F")
        bg = (color[0] // 4 + 191, color[1] // 4 + 191, color[2] // 4 + 191)
        self.set_fill_color(*bg)
        self.rect(x + 3, self.get_y(), w - 3, 18, "F")
        self.set_x(x + 10)
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*self.GRAY_700)
        y_start = self.get_y()
        self.set_y(y_start + 3)
        self.set_x(x + 10)
        self.multi_cell(w - 16, 4.5, text)
        self.set_y(y_start + 20)
        self.ln(2)

    def table_header(self, cols, widths):
        self.set_fill_color(*self.INDIGO)
        self.set_text_color(*self.WHITE)
        self.set_font("Helvetica", "B", 9)
        for i, col in enumerate(cols):
            self.cell(widths[i], 8, col, border=1, align="C", fill=True)
        self.ln()

    def table_row(self, cells, widths, fill=False):
        if fill:
            self.set_fill_color(*self.CODE_BG)
        else:
            self.set_fill_color(*self.WHITE)
        self.set_text_color(*self.GRAY_700)
        self.set_font("Helvetica", "", 9)
        for i, cell_text in enumerate(cells):
            self.cell(widths[i], 7, cell_text, border=1, align="C" if i > 0 else "L", fill=True)
        self.ln()


def build_pdf():
    pdf = TaskFlowDoc(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(20, 15, 20)

    # ===================== COVER PAGE =====================
    pdf.cover_page()

    # ===================== TABLE OF CONTENTS =====================
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*pdf.INDIGO)
    pdf.cell(0, 14, "Table of Contents", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    toc = [
        ("1", "Project Overview", "3"),
        ("2", "Technology Stack", "4"),
        ("3", "Project Structure", "5"),
        ("4", "Architecture Overview", "6"),
        ("5", "HTML Layer (index.html)", "8"),
        ("6", "CSS Architecture (style.css)", "11"),
        ("7", "JavaScript Architecture (app.js)", "15"),
        ("8", "Data Model & Storage", "20"),
        ("9", "Circular Progress Bar", "22"),
        ("10", "Chart.js Integration", "23"),
        ("11", "Theme System (Dark Mode)", "25"),
        ("12", "Responsive Design System", "26"),
        ("13", "Animation System", "28"),
        ("14", "Security Considerations", "29"),
        ("15", "Performance Notes", "29"),
        ("16", "Developer Guide", "30"),
    ]

    for num, title, page in toc:
        pdf.set_font("Helvetica", "B" if "." not in num else "", 11 if "." not in num else 10)
        pdf.set_text_color(*pdf.GRAY_700)
        dot_leader = "." * (70 - len(f"{num}  {title}"))
        pdf.set_x(25)
        pdf.cell(12, 7, num, new_x="END")
        pdf.cell(100, 7, title, new_x="END")
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*pdf.GRAY_400)
        pdf.cell(0, 7, page, align="R", new_x="LMARGIN", new_y="NEXT")

    # ===================== 1. PROJECT OVERVIEW =====================
    pdf.add_page()
    pdf.section_title("1", "Project Overview")

    pdf.body_text(
        "TaskFlow is a modern, full-featured task management web application built entirely with "
        "vanilla HTML, CSS, and JavaScript. It provides a professional-grade user experience with "
        "a dashboard layout, real-time analytics, data visualization, and a fully responsive design "
        "that works across all device sizes from desktop monitors to mobile phones."
    )

    pdf.body_text(
        "The application follows a client-side architecture where all data is persisted in the "
        "browser's localStorage API, requiring zero backend infrastructure. This makes it instantly "
        "deployable as a static site on any hosting platform."
    )

    pdf.subsection("Key Features")
    features = [
        "CRUD operations: Create, read, update (toggle), and delete tasks",
        "Priority system: Three levels (Low, Medium, High) with color-coded badges",
        "Circular SVG progress bar: Animated ring showing completion percentage",
        "Weekly activity bar chart: Tasks completed per day over the last 7 days (Chart.js)",
        "Task distribution doughnut chart: Visual split of completed vs pending tasks",
        "Real-time search: Instant text filtering as you type",
        "Multi-filter toolbar: Filter by status (All/Active/Completed) and priority",
        "Dark mode: Full theme toggle with localStorage persistence",
        "Responsive design: 4 breakpoints (desktop, tablet, mobile, small mobile)",
        "Data migration: Automatic upgrade from legacy localStorage format",
        "XSS protection: All user input is escaped before rendering",
        "Smooth animations: slideIn, slideOut, shake validation, hover micro-interactions",
        "Batch operations: Clear all completed tasks at once with animated removal",
    ]
    for f in features:
        pdf.bullet(f)

    # ===================== 2. TECHNOLOGY STACK =====================
    pdf.add_page()
    pdf.section_title("2", "Technology Stack")

    pdf.body_text(
        "TaskFlow is intentionally built with zero build tools and no npm dependencies. "
        "This makes it easy to clone, open, and run instantly in any browser."
    )

    widths = [45, 50, 75]
    pdf.table_header(["Technology", "Version", "Purpose"], widths)
    rows = [
        ("HTML5", "Living Standard", "Semantic structure, SVG graphics, ARIA attrs"),
        ("CSS3", "Living Standard", "Custom Properties, Grid, Flexbox, animations"),
        ("JavaScript", "ES6+", "Application logic, DOM manipulation, events"),
        ("Chart.js", "v4.x (CDN)", "Bar chart and doughnut chart rendering"),
        ("Google Fonts", "Inter", "Typography (weights 300-800)"),
        ("localStorage", "Web API", "Client-side data persistence"),
        ("SVG", "1.1", "Circular progress bar, inline icons"),
    ]
    for i, r in enumerate(rows):
        pdf.table_row(r, widths, fill=i % 2 == 0)

    pdf.ln(4)
    pdf.info_box(
        "Note: Chart.js is loaded from CDN (cdn.jsdelivr.net/npm/chart.js). "
        "If it fails to load, the app degrades gracefully - all features work except the two charts."
    )

    # ===================== 3. PROJECT STRUCTURE =====================
    pdf.add_page()
    pdf.section_title("3", "Project Structure")

    pdf.code_block(
        """taskflow-project/
|-- index.html              # Single-page application entry point
|-- css/
|   +-- style.css           # Complete stylesheet (1077 lines)
|-- js/
|   +-- app.js              # Application logic (512 lines)
|-- assets/
|   +-- images/
|       +-- check.png       # Legacy asset (unused, kept for history)
|-- docs/
|   +-- TaskFlow_Architecture.pdf   # This document
|-- .gitignore
|-- README.md""",
        title="Directory Tree"
    )

    pdf.body_text(
        "The project follows a classic separation of concerns with three core files:"
    )
    pdf.bullet("index.html - Structure and content (349 lines)")
    pdf.bullet("css/style.css - Presentation and responsive layout (1077 lines)")
    pdf.bullet("js/app.js - Behavior, state management, and charts (512 lines)")

    pdf.ln(2)
    pdf.body_text(
        "Total codebase size is approximately 1,940 lines of hand-written code. There is no build "
        "step, no bundler, and no transpilation. The code runs directly in the browser as-is."
    )

    # ===================== 4. ARCHITECTURE OVERVIEW =====================
    pdf.add_page()
    pdf.section_title("4", "Architecture Overview")

    pdf.body_text(
        "TaskFlow uses a straightforward Model-View-Controller-like pattern implemented "
        "in vanilla JavaScript. The architecture is designed for simplicity and maintainability."
    )

    pdf.subsection("4.1 High-Level Architecture Diagram")

    pdf.code_block(
        """+================================================================+
|                        BROWSER                                 |
|  +------------------+    +------------------+    +-----------+ |
|  |   index.html     |    |   css/style.css  |    | Chart.js  | |
|  |   (Structure)    |    |   (Presentation) |    | (CDN)     | |
|  +--------+---------+    +--------+---------+    +-----+-----+ |
|           |                       |                    |       |
|           +----------+------------+--------------------+       |
|                      |                                         |
|              +-------v--------+                                |
|              |   js/app.js    |                                |
|              |   (Behavior)   |                                |
|              +---+----+---+---+                                |
|                  |    |   |                                    |
|         +--------+  +-+  +--------+                            |
|         v           v             v                            |
|  +-----------+ +---------+ +------------+                      |
|  | DOM API   | | Storage | | Chart.js   |                      |
|  | Rendering | | API     | | Instances  |                      |
|  +-----------+ +---------+ +------------+                      |
|                     |                                          |
|              +------v------+                                   |
|              | localStorage|                                   |
|              | (JSON data) |                                   |
|              +-------------+                                   |
+================================================================+""",
        title="System Architecture"
    )

    pdf.subsection("4.2 Data Flow")

    pdf.code_block(
        """User Action (click/type/submit)
        |
        v
Event Handler (handleAddTask, handleTaskClick, etc.)
        |
        v
State Mutation (todos array modified)
        |
        +----> saveTodos() ----> localStorage.setItem()
        |
        v
render() function called
        |
        +----> renderTasks()      (rebuilds task list DOM)
        +----> updateStats()      (updates circle + stat cards)
        +----> updateCharts()     (refreshes Chart.js instances)""",
        title="Unidirectional Data Flow"
    )

    pdf.body_text(
        "Every user interaction follows the same unidirectional flow: Event -> State Mutation -> "
        "Save -> Re-render. This predictable pattern makes debugging straightforward: if the UI "
        "is wrong, check the state; if the state is wrong, check the event handler."
    )

    pdf.subsection("4.3 Module Organization")

    pdf.body_text(
        "Although contained in a single file (app.js), the code is organized into clearly "
        "separated sections using comment headers:"
    )

    widths2 = [45, 125]
    pdf.table_header(["Section", "Responsibility"], widths2)
    sections = [
        ("Constants", "Storage keys, configuration values"),
        ("State", "Global todos array, chart instance references"),
        ("DOM References", "Cached querySelector results in 'el' object"),
        ("Utilities", "generateId, escapeHtml, capitalize, formatDate"),
        ("Local Storage", "loadTodos (with migration), saveTodos"),
        ("Todo CRUD", "addTodo, toggleTodo, deleteTodo, clearCompleted"),
        ("Filtering", "getFilteredTodos with search + status + priority"),
        ("Rendering", "createTaskElement, renderTasks, updateStats, render"),
        ("Charts", "Chart.js init, update, weekly data, color helpers"),
        ("Theme", "initTheme, toggleTheme with chart color sync"),
        ("Event Handlers", "handleAddTask, handleTaskClick"),
        ("Initialization", "init() - wires everything on DOMContentLoaded"),
    ]
    for i, r in enumerate(sections):
        pdf.table_row(r, widths2, fill=i % 2 == 0)

    # ===================== 5. HTML LAYER =====================
    pdf.add_page()
    pdf.section_title("5", "HTML Layer (index.html)")

    pdf.body_text(
        "The HTML file is a single-page application with semantic elements. It defines the "
        "complete UI structure and relies on CSS for layout and JS for dynamic behavior."
    )

    pdf.subsection("5.1 Document Head")
    pdf.body_text(
        "The <head> section includes viewport meta for responsive design, Google Fonts preconnect "
        "for faster font loading, the Inter typeface (weights 300-800), and the main stylesheet."
    )

    pdf.subsection("5.2 Layout Structure")
    pdf.code_block(
        """<body>
  <header class="app-header">         <!-- Sticky gradient header -->
    +-- .brand                         <!-- Logo + title + date -->
    +-- .theme-btn                     <!-- Dark mode toggle -->
  </header>

  <div class="container app-layout">   <!-- CSS Grid: sidebar + main -->
    <aside class="sidebar">            <!-- Dashboard panel -->
      +-- .circle-card                 <!-- SVG circular progress -->
      +-- .stats-row                   <!-- 3x stat cards grid -->
      +-- .chart-card (weekly)         <!-- Bar chart canvas -->
      +-- .chart-card (status)         <!-- Doughnut chart canvas -->
    </aside>

    <main class="main-content">        <!-- Task management area -->
      +-- .add-form                    <!-- Input + priority selector -->
      +-- .toolbar                     <!-- Search + filters + clear -->
      +-- .tasks-section               <!-- Task list + empty state -->
    </main>
  </div>

  <script src="chart.js (CDN)">
  <script src="js/app.js">
</body>""",
        title="DOM Tree Overview"
    )

    pdf.subsection("5.3 SVG Circular Progress Bar (HTML)")
    pdf.body_text(
        "The circular progress bar is built with pure SVG. Two <circle> elements share the same "
        "center (cx=90, cy=90) and radius (r=75). The background circle uses a muted stroke, "
        "while the foreground circle uses an SVG linearGradient and the stroke-dasharray/"
        "stroke-dashoffset technique for animation."
    )

    pdf.code_block(
        """<svg class="circle-svg" viewBox="0 0 180 180">
  <defs>
    <linearGradient id="progress-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6366f1"/>    <!-- Indigo -->
      <stop offset="100%" stop-color="#06b6d4"/>   <!-- Cyan -->
    </linearGradient>
  </defs>
  <circle class="circle-bg" cx="90" cy="90" r="75"/>
  <circle class="circle-fg" cx="90" cy="90" r="75" id="circle-progress"/>
</svg>""",
        title="SVG Markup"
    )

    pdf.subsection("5.4 Priority Selector Pattern")
    pdf.body_text(
        "The priority selector uses hidden <input type='radio'> elements inside <label> wrappers. "
        "CSS uses the adjacent sibling selector (input:checked + .priority-tag) to style the "
        "active state. This is a pure CSS solution requiring zero JavaScript for visual feedback."
    )

    pdf.subsection("5.5 Accessibility")
    pdf.bullet("All interactive elements have aria-label attributes")
    pdf.bullet("SVG icons are decorative (no alt text needed, labels on parent buttons)")
    pdf.bullet("Form inputs have proper labels and autocomplete attributes")
    pdf.bullet("Semantic HTML: <header>, <main>, <aside>, <section>, <nav> elements")
    pdf.bullet("The theme toggle button has aria-label='Toggle theme'")

    # ===================== 6. CSS ARCHITECTURE =====================
    pdf.add_page()
    pdf.section_title("6", "CSS Architecture (style.css)")

    pdf.body_text(
        "The stylesheet is 1,077 lines organized into clearly commented sections. It uses "
        "CSS Custom Properties (variables) extensively for theming, and CSS Grid + Flexbox "
        "for all layout needs."
    )

    pdf.subsection("6.1 Design Token System (CSS Custom Properties)")
    pdf.body_text(
        "All visual values are centralized in :root as CSS Custom Properties. "
        "This enables instant theme switching by overriding variables in [data-theme='dark']."
    )

    pdf.code_block(
        """:root {
  /* Color Palette */
  --primary: #6366f1;        /* Indigo - brand color */
  --primary-dark: #4f46e5;   /* Hover state */
  --primary-light: #818cf8;  /* Focus rings */
  --primary-subtle: #eef2ff; /* Backgrounds */
  --accent: #06b6d4;         /* Cyan - progress gradient end */
  --success: #10b981;        /* Green - completed state */
  --warning: #f59e0b;        /* Amber - pending/medium priority */
  --danger: #ef4444;         /* Red - delete/high priority */

  /* Semantic Surface Colors */
  --bg: #f1f5f9;             /* Page background */
  --surface: #ffffff;        /* Card backgrounds */
  --text: #0f172a;           /* Primary text */
  --text-secondary: #475569; /* Secondary text */
  --text-muted: #94a3b8;     /* Muted/disabled text */
  --border: #e2e8f0;         /* Border color */

  /* Elevation (Shadow Scale) */
  --shadow-sm through --shadow-lg

  /* Spacing & Shape */
  --radius-sm: 8px;  --radius: 12px;  --radius-lg: 16px;

  /* Motion */
  --transition: 200ms cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);

  /* Layout Constants */
  --header-height: 72px;
  --sidebar-width: 340px;
}""",
        title="Design Tokens (Light Theme)"
    )

    pdf.subsection("6.2 Dark Theme Override")
    pdf.body_text(
        "Dark mode overrides every surface, text, border, and shadow variable. "
        "The subtle color variants use rgba() with low opacity for a natural dark-mode feel."
    )

    pdf.code_block(
        """[data-theme="dark"] {
  --bg: #0f172a;                              /* Slate-900 */
  --surface: #1e293b;                         /* Slate-800 */
  --text: #f1f5f9;                            /* Slate-100 */
  --text-secondary: #94a3b8;                  /* Slate-400 */
  --border: #334155;                          /* Slate-700 */
  --primary-subtle: rgba(99, 102, 241, 0.15); /* Translucent */
  --success-subtle: rgba(16, 185, 129, 0.15);
  /* ... shadows get heavier opacity ... */
}""",
        title="Dark Theme Overrides"
    )

    pdf.subsection("6.3 Layout System")

    pdf.subsubsection("Desktop Layout (> 1024px)")
    pdf.code_block(
        """.app-layout {
  display: grid;
  grid-template-columns: 340px 1fr;   /* Fixed sidebar + fluid main */
  gap: 28px;
  align-items: start;                  /* Sidebar sticks to top */
}

.sidebar {
  position: sticky;
  top: calc(var(--header-height) + 28px);  /* Below sticky header */
}""",
        title="Desktop Grid"
    )

    pdf.subsubsection("Tablet Layout (768px - 1024px)")
    pdf.code_block(
        """@media (max-width: 1024px) {
  .app-layout { grid-template-columns: 1fr; }   /* Single column */
  .sidebar {
    position: static;                             /* Not sticky */
    display: grid;
    grid-template-columns: 1fr 1fr;              /* Charts side by side */
  }
  .circle-card, .stats-row { grid-column: 1/-1; } /* Full width */
}""",
        title="Tablet Breakpoint"
    )

    pdf.subsubsection("Mobile Layout (< 768px)")
    pdf.body_text(
        "On mobile, everything stacks vertically. The add button becomes icon-only, "
        "the toolbar stacks, delete buttons are always visible (no hover on touch), "
        "and the circular progress bar shrinks to 150px."
    )

    pdf.subsection("6.4 Circular Progress Bar (CSS)")

    pdf.code_block(
        """.circle-svg {
  width: 180px; height: 180px;
  transform: rotate(-90deg);          /* Start from 12 o'clock */
}

.circle-fg {
  fill: none;
  stroke: url(#progress-gradient);     /* SVG gradient reference */
  stroke-width: 8;
  stroke-linecap: round;               /* Rounded endpoints */
  stroke-dasharray: 471.24;            /* Circumference = 2 * PI * 75 */
  stroke-dashoffset: 471.24;           /* 100% hidden initially */
  transition: stroke-dashoffset 1s cubic-bezier(0.4, 0, 0.2, 1);
}""",
        title="SVG Circle Technique"
    )

    pdf.info_box(
        "Math: circumference = 2 * PI * radius = 2 * 3.14159 * 75 = 471.24. "
        "To show N% progress: stroke-dashoffset = 471.24 * (1 - N/100). "
        "At 0%: offset = 471.24 (fully hidden). At 100%: offset = 0 (fully visible).",
        color=pdf.ACCENT
    )

    # ===================== 7. JAVASCRIPT ARCHITECTURE =====================
    pdf.add_page()
    pdf.section_title("7", "JavaScript Architecture (app.js)")

    pdf.body_text(
        "The JavaScript layer is 512 lines of vanilla ES6+ code organized into 12 logical "
        "sections. It manages application state, DOM rendering, chart integration, theme "
        "switching, and all user interactions."
    )

    pdf.subsection("7.1 State Management")

    pdf.code_block(
        """// Global state
let todos = [];              // Array of todo objects (source of truth)
let weeklyChart = null;      // Chart.js bar chart instance
let statusChart = null;      // Chart.js doughnut chart instance

// DOM element cache (queried once at load time)
const el = {
  addForm: $("#add-form"),
  taskInput: $("#task-input"),
  tasksList: $("#tasks-list"),
  circleProgress: $("#circle-progress"),
  // ... 14 more cached references
};""",
        title="State & DOM Cache"
    )

    pdf.body_text(
        "The 'todos' array is the single source of truth. The UI is always derived from it. "
        "DOM references are cached in the 'el' object at load time to avoid repeated "
        "querySelector calls during renders."
    )

    pdf.subsection("7.2 Todo Data Model")

    pdf.code_block(
        """{
  id: "m2abc1234xyz",           // Unique ID (timestamp + random base36)
  text: "Buy groceries",        // Task description (user input, escaped)
  completed: false,             // Boolean completion state
  priority: "medium",           // "low" | "medium" | "high"
  createdAt: "2026-02-08T...",  // ISO 8601 creation timestamp
  completedAt: null             // ISO 8601 completion timestamp (or null)
}""",
        title="Todo Object Schema"
    )

    pdf.body_text(
        "The completedAt timestamp is critical for the weekly activity chart. When a task is "
        "toggled complete, the current timestamp is stored. When uncompleted, it's set back to "
        "null. This enables accurate historical tracking of completion activity."
    )

    pdf.subsection("7.3 CRUD Operations")

    pdf.subsubsection("addTodo(text, priority)")
    pdf.body_text(
        "Creates a new todo object with a generated ID and current timestamps, prepends it "
        "to the todos array (unshift for newest-first ordering), saves to localStorage, "
        "and triggers a full re-render."
    )

    pdf.subsubsection("toggleTodo(id)")
    pdf.body_text(
        "Finds the todo by ID, flips the completed boolean, sets or clears the completedAt "
        "timestamp, saves, and re-renders. The completedAt timestamp feeds the weekly chart."
    )

    pdf.subsubsection("deleteTodo(id)")
    pdf.body_text(
        "Filters the todo out of the array and saves. The re-render is handled by the "
        "caller after the slide-out animation completes (via animationend event)."
    )

    pdf.subsubsection("clearCompleted()")
    pdf.body_text(
        "Adds the 'slide-out' CSS class to all completed task DOM elements, waits 350ms for "
        "the animation, then bulk-removes completed todos from state and re-renders."
    )

    pdf.subsection("7.4 Rendering Pipeline")

    pdf.code_block(
        """function render() {
  renderTasks();     // 1. Rebuild task list from filtered state
  updateStats();     // 2. Update stat cards + circle progress
  updateCharts();    // 3. Push new data to Chart.js instances
}

function renderTasks() {
  const filtered = getFilteredTodos();  // Apply search + filters
  el.tasksList.innerHTML = "";          // Clear current DOM
  filtered.forEach(todo => {
    el.tasksList.appendChild(createTaskElement(todo));
  });
  el.emptyState.classList.toggle("visible", filtered.length === 0);
}

function updateStats() {
  // Calculate totals
  const total = todos.length;
  const done = todos.filter(t => t.completed).length;
  const percent = total ? Math.round((done / total) * 100) : 0;

  // Update DOM text
  el.statTotal.textContent = total;
  el.statDone.textContent = done;
  el.statPending.textContent = total - done;

  // Update circular progress bar
  const circumference = 2 * Math.PI * 75;
  const offset = circumference * (1 - percent / 100);
  el.circleProgress.style.strokeDashoffset = offset;
  el.circlePercent.textContent = percent + "%";
}""",
        title="Render Pipeline"
    )

    pdf.subsection("7.5 Filtering System")

    pdf.code_block(
        """function getFilteredTodos() {
  const search = el.searchInput.value.toLowerCase().trim();
  const status = el.filterStatus.value;     // "all"|"active"|"completed"
  const priority = el.filterPriority.value; // "all"|"low"|"medium"|"high"

  return todos.filter(todo => {
    const matchSearch = !search || todo.text.toLowerCase().includes(search);
    const matchStatus = status === "all" ||
      (status === "active" && !todo.completed) ||
      (status === "completed" && todo.completed);
    const matchPriority = priority === "all" || todo.priority === priority;
    return matchSearch && matchStatus && matchPriority;
  });
}""",
        title="Multi-criteria Filtering"
    )

    pdf.body_text(
        "Filters compose cleanly: each criterion returns true if 'all' is selected, or checks "
        "the specific match. The search input triggers renderTasks on every keystroke (input event) "
        "for real-time feedback. The dropdown filters trigger on the change event."
    )

    pdf.subsection("7.6 Event Delegation")

    pdf.body_text(
        "Instead of attaching event listeners to every task button, a single listener on the "
        "task list container uses event delegation with Element.closest() to determine what "
        "was clicked. This is more performant and automatically handles dynamically added tasks."
    )

    pdf.code_block(
        """function handleTaskClick(e) {
  const deleteBtn = e.target.closest(".task-delete");
  const checkBtn = e.target.closest(".task-check");
  const taskItem = e.target.closest(".task-item");

  if (!taskItem) return;

  if (deleteBtn) {
    taskItem.classList.add("slide-out");       // Trigger CSS animation
    taskItem.addEventListener("animationend", () => {
      deleteTodo(taskItem.dataset.id);         // Remove from state
      render();                                 // Re-render
    });
  } else if (checkBtn) {
    toggleTodo(taskItem.dataset.id);           // Toggle + re-render
  }
}

// Single listener for all tasks
el.tasksList.addEventListener("click", handleTaskClick);""",
        title="Event Delegation Pattern"
    )

    # ===================== 8. DATA MODEL & STORAGE =====================
    pdf.add_page()
    pdf.section_title("8", "Data Model & Storage")

    pdf.subsection("8.1 localStorage Schema")

    pdf.code_block(
        """Key: "taskflow_todos"
Value: JSON array of todo objects

Example:
[
  {
    "id": "m2abc1234xyz",
    "text": "Finish quarterly report",
    "completed": true,
    "priority": "high",
    "createdAt": "2026-02-07T09:30:00.000Z",
    "completedAt": "2026-02-08T14:22:00.000Z"
  },
  {
    "id": "m2def5678abc",
    "text": "Buy milk",
    "completed": false,
    "priority": "low",
    "createdAt": "2026-02-08T08:00:00.000Z",
    "completedAt": null
  }
]

Key: "taskflow_theme"
Value: "light" or "dark" """,
        title="localStorage Keys"
    )

    pdf.subsection("8.2 Legacy Data Migration")

    pdf.body_text(
        "The previous version of the app stored todos as a simple array of strings under the "
        "key 'todos'. The loadTodos() function automatically detects and migrates this format:"
    )

    pdf.code_block(
        """function loadTodos() {
  // 1. Try new format first
  const data = localStorage.getItem(STORAGE_KEY);
  if (data) return JSON.parse(data);

  // 2. Check for legacy format
  const legacy = localStorage.getItem("todos");
  if (legacy) {
    const items = JSON.parse(legacy);
    const migrated = items.map(text => ({
      id: generateId(),
      text: typeof text === "string" ? text : String(text),
      completed: false,
      priority: "medium",
      createdAt: new Date().toISOString(),
      completedAt: null,
    }));
    saveTodos(migrated);               // Save in new format
    localStorage.removeItem("todos");  // Clean up legacy key
    return migrated;
  }

  return [];  // Fresh start
}""",
        title="Migration Logic"
    )

    pdf.info_box(
        "The migration is transparent to the user. On first load after upgrade, legacy tasks "
        "appear with 'Medium' priority and today's date. The old 'todos' key is removed.",
        color=pdf.SUCCESS
    )

    pdf.subsection("8.3 ID Generation")

    pdf.code_block(
        """function generateId() {
  return Date.now().toString(36) + Math.random().toString(36).substr(2, 9);
}
// Example output: "m2k7f3a1x" + "abc123def" = "m2k7f3a1xabc123def" """,
        title="Unique ID Strategy"
    )

    pdf.body_text(
        "IDs combine a base-36 timestamp with random characters, ensuring uniqueness even "
        "if multiple tasks are created in the same millisecond."
    )

    # ===================== 9. CIRCULAR PROGRESS BAR =====================
    pdf.add_page()
    pdf.section_title("9", "Circular Progress Bar")

    pdf.body_text(
        "The circular progress bar is one of the most visually prominent features. It's built "
        "entirely with SVG and CSS - no canvas, no library."
    )

    pdf.subsection("9.1 How It Works")

    pdf.body_text("The technique uses three SVG/CSS properties working together:")
    pdf.bullet("stroke-dasharray: Sets the total length of the dash pattern (= circumference)")
    pdf.bullet("stroke-dashoffset: Controls how much of the stroke is hidden")
    pdf.bullet("transform: rotate(-90deg): Rotates the circle so 0% starts at 12 o'clock")

    pdf.ln(2)
    pdf.body_text("The math is simple:")
    pdf.code_block(
        """Circumference = 2 * PI * radius = 2 * 3.14159 * 75 = 471.24

For a given completion percentage:
  offset = circumference * (1 - percent / 100)

Examples:
  0% complete   -> offset = 471.24 * (1 - 0)    = 471.24 (circle hidden)
  25% complete  -> offset = 471.24 * (1 - 0.25)  = 353.43
  50% complete  -> offset = 471.24 * (1 - 0.50)  = 235.62
  75% complete  -> offset = 471.24 * (1 - 0.75)  = 117.81
  100% complete -> offset = 471.24 * (1 - 1.0)   = 0      (full circle)""",
        title="Offset Calculation"
    )

    pdf.subsection("9.2 Gradient Effect")
    pdf.body_text(
        "The stroke uses an SVG <linearGradient> that transitions from Indigo (#6366f1) "
        "to Cyan (#06b6d4). This gradient is defined in the <defs> section of the SVG and "
        "referenced via stroke: url(#progress-gradient) in CSS."
    )

    pdf.subsection("9.3 Animation")
    pdf.body_text(
        "The CSS transition property on stroke-dashoffset provides smooth animation whenever "
        "the value changes. The 1-second cubic-bezier easing creates a satisfying deceleration "
        "effect as the progress ring fills or empties."
    )

    # ===================== 10. CHART.JS INTEGRATION =====================
    pdf.add_page()
    pdf.section_title("10", "Chart.js Integration")

    pdf.subsection("10.1 Weekly Activity Bar Chart")

    pdf.body_text(
        "The bar chart shows the number of tasks completed per day over the last 7 days. "
        "Data is computed from the completedAt timestamps in the todos array."
    )

    pdf.code_block(
        """function getWeeklyData() {
  const labels = [], data = [];
  for (let i = 6; i >= 0; i--) {
    const date = new Date();
    date.setHours(0, 0, 0, 0);
    date.setDate(date.getDate() - i);

    labels.push(date.toLocaleDateString("en-US", { weekday: "short" }));

    const nextDay = new Date(date);
    nextDay.setDate(nextDay.getDate() + 1);

    const count = todos.filter(t => {
      if (!t.completedAt) return false;
      const d = new Date(t.completedAt);
      return d >= date && d < nextDay;    // Day boundary check
    }).length;
    data.push(count);
  }
  return { labels, data };
}""",
        title="Weekly Data Computation"
    )

    pdf.body_text(
        "Chart configuration: borderRadius: 8 for rounded bar tops, maxBarThickness: 32px, "
        "no legend, custom tooltip with task count. Y-axis uses stepSize: 1 for integer ticks."
    )

    pdf.subsection("10.2 Task Distribution Doughnut Chart")

    pdf.body_text(
        "The doughnut chart shows the split between completed and pending tasks. "
        "Colors: green (#10b981) for completed, amber (#f59e0b) for pending. "
        "The cutout is 72% creating a thin ring. When there are no tasks, a single "
        "gray segment displays with a 'No tasks' label."
    )

    pdf.subsection("10.3 Theme-Aware Chart Updates")

    pdf.body_text(
        "When the user toggles dark mode, chart colors must update. The toggleTheme() "
        "function recalculates grid colors, text colors, and legend colors, then calls "
        "chart.update() to repaint."
    )

    pdf.code_block(
        """function getChartColors() {
  const isDark = document.documentElement.dataset.theme === "dark";
  return {
    gridColor: isDark ? "rgba(148,163,184,0.08)" : "rgba(0,0,0,0.06)",
    textColor: isDark ? "#94a3b8" : "#64748b",
  };
}""",
        title="Dynamic Chart Colors"
    )

    pdf.subsection("10.4 Graceful Degradation")
    pdf.body_text(
        "Chart initialization is wrapped in a try/catch block and checks for "
        "typeof Chart === 'undefined'. If Chart.js fails to load from CDN, the rest of "
        "the app continues to work normally. Only the two chart canvases remain empty."
    )

    # ===================== 11. THEME SYSTEM =====================
    pdf.add_page()
    pdf.section_title("11", "Theme System (Dark Mode)")

    pdf.body_text(
        "The theme system uses HTML data attributes and CSS Custom Property overrides for "
        "a zero-flicker, JavaScript-controlled dark mode."
    )

    pdf.subsection("11.1 How It Works")

    pdf.code_block(
        """1. <html data-theme="light">      (default)

2. CSS variables defined in :root   (light values)
   CSS overrides in [data-theme="dark"]  (dark values)

3. User clicks theme toggle button

4. JS toggles: document.documentElement.dataset.theme = "dark"

5. ALL CSS variables instantly update  (no class toggling per element)

6. CSS transition on body smooths the color change:
   transition: background 400ms, color 400ms

7. Preference saved: localStorage.setItem("taskflow_theme", "dark")

8. On next page load, initTheme() reads and applies saved preference""",
        title="Theme Toggle Flow"
    )

    pdf.subsection("11.2 Icon Toggle")
    pdf.body_text(
        "The theme button contains both a sun and moon SVG icon. CSS controls visibility:"
    )

    pdf.code_block(
        """[data-theme="light"] .icon-sun  { display: none; }
[data-theme="light"] .icon-moon { display: block; }
[data-theme="dark"]  .icon-sun  { display: block; }
[data-theme="dark"]  .icon-moon { display: none; }""",
        title="Icon Toggle CSS"
    )

    # ===================== 12. RESPONSIVE DESIGN =====================
    pdf.add_page()
    pdf.section_title("12", "Responsive Design System")

    pdf.body_text(
        "The application supports four layout tiers with media query breakpoints. "
        "The approach is desktop-first: the default styles target wide screens, "
        "and max-width media queries progressively adapt for smaller devices."
    )

    widths3 = [32, 30, 50, 58]
    pdf.table_header(["Breakpoint", "Target", "Layout", "Key Changes"], widths3)
    rows3 = [
        ("> 1024px", "Desktop", "Sidebar + Main grid", "Sticky sidebar, full features"),
        ("768-1024", "Tablet", "Single column", "Sidebar becomes 2-col grid"),
        ("481-768", "Mobile", "Single column", "Icon-only btn, stacked toolbar"),
        ("< 480px", "Sm. Mobile", "Single column", "Compact spacing, 130px circle"),
    ]
    for i, r in enumerate(rows3):
        pdf.table_row(r, widths3, fill=i % 2 == 0)

    pdf.ln(4)

    pdf.subsection("12.1 Desktop (> 1024px)")
    pdf.bullet("Two-column CSS Grid: 340px sidebar + fluid main content")
    pdf.bullet("Sidebar is position: sticky, scrolls with content but stays visible")
    pdf.bullet("Circular progress bar at 180x180px")
    pdf.bullet("Full 'Add Task' button with text label")
    pdf.bullet("Delete buttons hidden until hover")

    pdf.subsection("12.2 Tablet (768px - 1024px)")
    pdf.bullet("Grid collapses to single column")
    pdf.bullet("Sidebar becomes a 2-column grid (charts side by side)")
    pdf.bullet("Circle card and stats row span full width")
    pdf.bullet("Sidebar is no longer sticky")

    pdf.subsection("12.3 Mobile (< 768px)")
    pdf.bullet("Header height reduces from 72px to 64px")
    pdf.bullet("Container padding reduces from 24px to 16px")
    pdf.bullet("Sidebar becomes fully stacked (single column)")
    pdf.bullet("Circular progress bar shrinks to 150x150px")
    pdf.bullet("Add button becomes icon-only (text hidden)")
    pdf.bullet("Toolbar stacks vertically, filters stretch full width")
    pdf.bullet("Delete buttons always visible (no hover on touch devices)")

    pdf.subsection("12.4 Small Mobile (< 480px)")
    pdf.bullet("Container padding further reduces to 12px")
    pdf.bullet("Brand text shrinks to 1.1rem")
    pdf.bullet("Circular progress bar shrinks to 130x130px, percentage to 1.6rem")
    pdf.bullet("Stat cards get tighter padding")
    pdf.bullet("Chart heights reduce for better viewport usage")

    # ===================== 13. ANIMATION SYSTEM =====================
    pdf.add_page()
    pdf.section_title("13", "Animation System")

    pdf.body_text(
        "TaskFlow uses CSS keyframe animations and transitions for all motion. "
        "No JavaScript animation libraries are used."
    )

    widths4 = [35, 40, 95]
    pdf.table_header(["Animation", "Trigger", "Description"], widths4)
    rows4 = [
        ("slideIn", "Task added", "Fades in + slides down from -10px (0.35s)"),
        ("slideOut", "Task deleted", "Fades out + slides right 50px, collapses (0.35s)"),
        ("shake", "Empty input", "Horizontal shake -6/+6px (0.4s)"),
        ("Stroke offset", "Stats change", "Circle ring fills/empties smoothly (1s)"),
        ("Hover lift", "Mouse enter", "translateY(-1px) + shadow on task items"),
        ("Check pop", "Toggle done", "Checkbox scale 0.3 -> 1.0 with opacity"),
        ("Theme fade", "Mode toggle", "Background/color transitions over 400ms"),
        ("Button press", "Click", "scale(0.97) on active state"),
    ]
    for i, r in enumerate(rows4):
        pdf.table_row(r, widths4, fill=i % 2 == 0)

    pdf.ln(4)
    pdf.body_text(
        "All animations use cubic-bezier(0.4, 0, 0.2, 1) easing, which is the Material Design "
        "'standard' curve. This provides a natural deceleration feel."
    )

    # ===================== 14. SECURITY =====================
    pdf.section_title("14", "Security Considerations")

    pdf.bullet("XSS Prevention: All user-entered task text is escaped via escapeHtml() before being "
               "inserted into innerHTML. This function creates a temporary DOM text node to safely "
               "convert special characters to HTML entities.")
    pdf.bullet("No eval() or Function(): The codebase never uses eval or dynamic code execution.")
    pdf.bullet("No external data ingestion: The app only reads from localStorage (same-origin). "
               "There are no API calls, fetch requests, or external data sources.")
    pdf.bullet("CDN integrity: Chart.js is loaded from jsdelivr CDN. For production, consider "
               "adding Subresource Integrity (SRI) hash attributes to the script tag.")
    pdf.bullet("localStorage limits: ~5MB per origin. For a todo app, this is more than sufficient "
               "(thousands of tasks). No sensitive data is stored.")

    # ===================== 15. PERFORMANCE =====================
    pdf.add_page()
    pdf.section_title("15", "Performance Notes")

    pdf.bullet("DOM caching: All querySelector calls happen once at init time and are stored in "
               "the 'el' object. Subsequent accesses are O(1) property lookups.")
    pdf.bullet("Event delegation: A single click listener on the task list handles all task "
               "interactions, regardless of how many tasks exist.")
    pdf.bullet("Chart.js update('none'): Charts are updated with animation disabled during "
               "normal data changes to prevent janky transitions on every keystroke.")
    pdf.bullet("Font preconnect: Google Fonts uses <link rel='preconnect'> to establish early "
               "connections, reducing font load latency.")
    pdf.bullet("Minimal reflows: The render() function clears and rebuilds the task list in "
               "a single innerHTML = '' + appendChild loop, minimizing layout thrashing.")
    pdf.bullet("CSS containment: Cards use overflow: hidden, which allows the browser to "
               "optimize paint operations.")
    pdf.bullet("No framework overhead: Zero library code for DOM management. The entire JS "
               "payload is ~512 lines (~12KB unminified).")

    # ===================== 16. DEVELOPER GUIDE =====================
    pdf.section_title("16", "Developer Guide")

    pdf.subsection("16.1 Getting Started")

    pdf.code_block(
        """# Clone the repository
git clone <repo-url>
cd taskflow-project

# Open in browser (no build step needed)
# Option A: Double-click index.html
# Option B: Use a local server
npx serve .
# or
python -m http.server 8000""",
        title="Quick Start"
    )

    pdf.subsection("16.2 Adding a New Feature")

    pdf.body_text("Follow these steps to add a new feature (example: due dates):")
    pdf.bullet("1. Extend the todo schema in addTodo() with a new field (e.g., dueDate: null)")
    pdf.bullet("2. Add UI elements to the add-form in index.html (e.g., date picker input)")
    pdf.bullet("3. Update createTaskElement() to render the new field in the task item")
    pdf.bullet("4. Add CSS styles in style.css for the new UI elements")
    pdf.bullet("5. Update getFilteredTodos() if the new field should be filterable")
    pdf.bullet("6. Test the legacy migration - old todos without the field should work")

    pdf.subsection("16.3 Adding a New Chart")

    pdf.body_text("To add a new chart (example: priority distribution):")
    pdf.bullet("1. Add a <canvas> element inside a .chart-card in the sidebar HTML")
    pdf.bullet("2. Add a DOM reference in the 'el' object")
    pdf.bullet("3. Create a data computation function (e.g., getPriorityData())")
    pdf.bullet("4. Initialize the chart in initCharts()")
    pdf.bullet("5. Update it in updateCharts()")
    pdf.bullet("6. Handle theme colors in toggleTheme()")

    pdf.subsection("16.4 Modifying the Color Scheme")

    pdf.body_text(
        "All colors are defined as CSS Custom Properties in :root (light) and "
        "[data-theme='dark'] (dark). To change the brand color from indigo to blue:"
    )

    pdf.code_block(
        """/* Change in :root */
--primary: #3b82f6;       /* Blue-500 instead of Indigo-500 */
--primary-dark: #2563eb;  /* Blue-600 */
--primary-light: #60a5fa; /* Blue-400 */
--primary-subtle: #eff6ff; /* Blue-50 */

/* Also update the SVG gradient in index.html */
<stop offset="0%" stop-color="#3b82f6"/>""",
        title="Color Scheme Change"
    )

    pdf.subsection("16.5 Key Files Quick Reference")

    widths5 = [55, 115]
    pdf.table_header(["What to change", "Where to look"], widths5)
    rows5 = [
        ("App name/branding", "index.html line 36, <h1>TaskFlow</h1>"),
        ("Color palette", "css/style.css :root variables (lines 10-55)"),
        ("Dark mode colors", "css/style.css [data-theme='dark'] (lines 58-83)"),
        ("Layout breakpoints", "css/style.css @media queries (lines 874+)"),
        ("Todo data schema", "js/app.js addTodo() function (line 93)"),
        ("Chart config", "js/app.js initCharts() function (line 253)"),
        ("Storage key", "js/app.js STORAGE_KEY constant (line 2)"),
        ("Progress bar math", "js/app.js updateStats() (line 204)"),
        ("Priority options", "index.html priority-group (line 238)"),
    ]
    for i, r in enumerate(rows5):
        pdf.table_row(r, widths5, fill=i % 2 == 0)

    # ===================== FINAL PAGE =====================
    pdf.add_page()
    pdf.ln(30)
    pdf.set_fill_color(*pdf.INDIGO)
    pdf.rect(0, pdf.get_y() - 10, 210, 70, "F")
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*pdf.WHITE)
    pdf.cell(0, 14, "TaskFlow", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(200, 200, 255)
    pdf.cell(0, 8, "Architecture Documentation v2.0", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, f"Generated on {datetime.date.today().strftime('%B %d, %Y')}", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.set_y(pdf.get_y() + 30)
    pdf.set_text_color(*pdf.GRAY_700)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, "Built with HTML5, CSS3, JavaScript ES6+, and Chart.js", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(*pdf.GRAY_500)
    pdf.cell(0, 6, "Zero dependencies. Zero build tools. Pure web standards.", align="C", new_x="LMARGIN", new_y="NEXT")

    return pdf


if __name__ == "__main__":
    import os
    pdf = build_pdf()
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "TaskFlow_Architecture.pdf")
    pdf.output(out_path)
    print(f"PDF generated successfully: {out_path}")
    print(f"Total pages: {pdf.page_no()}")
