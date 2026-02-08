<div align="center">

# TaskFlow

### Smart Todo Manager with Analytics Dashboard

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)

<br/>

A professional-grade, full-featured task management application built with **zero dependencies** and **zero build tools** &mdash; pure vanilla HTML, CSS, and JavaScript. Features a real-time analytics dashboard with circular progress bar, interactive charts, dark mode, and a fully responsive design from desktop to mobile.

<br/>

**[Live Demo](#-quick-start)** &nbsp;&middot;&nbsp; **[Documentation](docs/TaskFlow_Architecture.pdf)** &nbsp;&middot;&nbsp; **[Report Bug](https://github.com/danialeyz/todolist-project/issues)** &nbsp;&middot;&nbsp; **[Request Feature](https://github.com/danialeyz/todolist-project/issues)**

<br/>

<table>
<tr>
<td width="50%">

**Light Mode**

```
+----------------------------------+
|  TaskFlow         [date]    [D]  |
+----------+-----------------------+
|  [==O==] |  [+ What needs...]    |
|   67%    |  Priority: Lo Med Hi  |
|  Complete|                       |
|          |  [Search...] [Filter] |
|  3  2  1 |                       |
| Tot Don Pen  [ ] Buy groceries   |
|          |  [x] Finish report    |
|  Weekly  |  [ ] Call dentist     |
|  |||.|   |  [x] Email team       |
|  |||.|   |  [ ] Read chapter 5   |
|  Status  |                       |
|  [==O==] |                       |
+----------+-----------------------+
```

</td>
<td width="50%">

**Dark Mode**

```
+----------------------------------+
|  TaskFlow         [date]    [L]  |
+----------+-----------------------+
|  [==O==] |  [+ What needs...]    |
|   67%    |  Priority: Lo Med Hi  |
|  Complete|                       |
|          |  [Search...] [Filter] |
|  3  2  1 |                       |
| Tot Don Pen  [ ] Buy groceries   |
|          |  [x] Finish report    |
|  Weekly  |  [ ] Call dentist     |
|  |||.|   |  [x] Email team       |
|  |||.|   |  [ ] Read chapter 5   |
|  Status  |                       |
|  [==O==] |                       |
+----------+-----------------------+
```

</td>
</tr>
</table>

</div>

---

## Highlights

<table>
<tr>
<td align="center" width="25%">
<br/>
<img width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg"/>
<br/><br/>
<b>Zero Dependencies</b>
<br/>
No npm, no node_modules, no webpack. Open <code>index.html</code> and it just works.
<br/><br/>
</td>
<td align="center" width="25%">
<br/>
<img width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg"/>
<br/><br/>
<b>Fully Responsive</b>
<br/>
4 breakpoints: desktop, tablet, mobile, small mobile. Pixel-perfect at every size.
<br/><br/>
</td>
<td align="center" width="25%">
<br/>
<img width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"/>
<br/><br/>
<b>Real-Time Analytics</b>
<br/>
Circular progress bar, weekly activity chart, and task distribution doughnut.
<br/><br/>
</td>
<td align="center" width="25%">
<br/>
<img width="60" src="https://www.chartjs.org/img/chartjs-logo.svg"/>
<br/><br/>
<b>Dark Mode</b>
<br/>
One-click theme toggle with smooth transitions. Preference saved to localStorage.
<br/><br/>
</td>
</tr>
</table>

---

## Features

### Task Management
- **Create tasks** with a priority level (Low / Medium / High)
- **Complete tasks** with animated checkbox and strikethrough effect
- **Delete tasks** with smooth slide-out animation
- **Batch clear** all completed tasks at once
- **Persistent storage** &mdash; tasks survive page refresh via localStorage

### Analytics Dashboard
- **Circular SVG progress bar** &mdash; gradient ring (indigo-to-cyan) with animated fill, showing completion percentage in real-time
- **Stat cards** &mdash; Total, Done, and Pending counts with color-coded icons
- **Weekly activity bar chart** &mdash; tasks completed per day for the last 7 days (Chart.js)
- **Task distribution doughnut chart** &mdash; visual split of completed vs. pending tasks

### Search & Filtering
- **Real-time search** &mdash; instant text filtering as you type
- **Status filter** &mdash; All Tasks / Active / Completed
- **Priority filter** &mdash; All / High / Medium / Low
- Filters combine seamlessly (e.g., search "report" + status "active" + priority "high")

### Design & UX
- **Dark mode** with one-click toggle and persistent preference
- **4 responsive breakpoints** (desktop > tablet > mobile > small mobile)
- **Sticky sidebar** on desktop so the dashboard stays visible while scrolling tasks
- **Smooth animations** &mdash; slideIn, slideOut, shake validation, hover micro-interactions, check pop
- **Accessible** &mdash; semantic HTML, ARIA labels, keyboard-friendly

---

## Tech Stack

| Technology | Purpose |
|:---|:---|
| **HTML5** | Semantic structure, SVG graphics, ARIA accessibility |
| **CSS3** | Custom Properties (theming), CSS Grid, Flexbox, keyframe animations |
| **JavaScript ES6+** | State management, DOM rendering, event delegation |
| **Chart.js 4.x** | Bar chart and doughnut chart (loaded from CDN) |
| **Google Fonts** | Inter typeface (weights 300&ndash;800) |
| **localStorage API** | Client-side data persistence |
| **SVG** | Circular progress bar, all inline icons |

> **No build tools.** No npm. No webpack. No transpilation. The code runs directly in the browser as-is.

---

## Architecture

```
                    +=====================+
                    |     index.html      |
                    |    (349 lines)      |
                    +=========+==========+
                              |
               +--------------+--------------+
               |                             |
      +--------v--------+          +--------v--------+
      |  css/style.css  |          |    js/app.js    |
      |  (1,077 lines)  |          |   (512 lines)   |
      +-----------------+          +---+----+----+---+
                                       |    |    |
                              +--------+  +-+  +-+-------+
                              |           |              |
                        +-----v---+ +-----v----+ +------v-----+
                        | DOM API | | Storage  | | Chart.js   |
                        +---------+ +-----+----+ +------------+
                                          |
                                   +------v------+
                                   | localStorage|
                                   +-------------+
```

### Data Flow

Every user action follows the same **unidirectional** pattern:

```
User Action  -->  Event Handler  -->  State Mutation  -->  Save  -->  Re-render
  (click)        (handleAddTask)     (todos.unshift)   (saveTodos)   (render)
```

### Data Model

Each task is stored as a rich object:

```json
{
  "id": "m2abc1234xyz",
  "text": "Finish quarterly report",
  "completed": true,
  "priority": "high",
  "createdAt": "2026-02-07T09:30:00.000Z",
  "completedAt": "2026-02-08T14:22:00.000Z"
}
```

| Field | Type | Description |
|:---|:---|:---|
| `id` | `string` | Unique identifier (base36 timestamp + random) |
| `text` | `string` | Task description (HTML-escaped on render) |
| `completed` | `boolean` | Completion state |
| `priority` | `string` | `"low"` \| `"medium"` \| `"high"` |
| `createdAt` | `string` | ISO 8601 creation timestamp |
| `completedAt` | `string\|null` | ISO 8601 completion timestamp (drives weekly chart) |

---

## Project Structure

```
taskflow-project/
├── index.html                          # Single-page application (349 lines)
├── css/
│   └── style.css                       # Full stylesheet with dark mode (1,077 lines)
├── js/
│   └── app.js                          # Application logic & charts (512 lines)
├── assets/
│   └── images/
│       └── check.png                   # Legacy asset (preserved for git history)
├── docs/
│   └── TaskFlow_Architecture.pdf       # 27-page architecture documentation
├── generate_docs.py                    # PDF documentation generator script
├── .gitignore
└── README.md                           # You are here
```

**Total: ~1,940 lines of hand-written code across 3 core files.**

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/danialeyz/todolist-project.git
cd todolist-project

# 2. Open in browser (pick one)
start index.html                # Windows
open index.html                 # macOS
xdg-open index.html             # Linux

# Or use any local server:
npx serve .
# or
python -m http.server 8000
```

> **That's it.** No `npm install`. No build step. No configuration. Just open and use.

---

## Responsive Design

The application adapts across **4 breakpoints** with a desktop-first approach:

| Breakpoint | Target | Layout | Key Adaptations |
|:---|:---|:---|:---|
| **> 1024px** | Desktop | Sidebar + Main grid | Sticky sidebar, full button labels, hover delete |
| **768&ndash;1024px** | Tablet | Single column | Sidebar becomes 2-column grid, charts side-by-side |
| **481&ndash;768px** | Mobile | Stacked | Icon-only add btn, stacked toolbar, always-visible delete |
| **< 480px** | Small Mobile | Compact | 130px progress ring, tighter spacing, smaller text |

---

## Dark Mode

Toggle with the **moon/sun** button in the header. The entire UI transitions smoothly in 400ms.

**How it works:**
1. `<html data-theme="light|dark">` controls the active theme
2. CSS Custom Properties in `:root` (light) are overridden by `[data-theme="dark"]`
3. **Every** color, shadow, and border updates instantly &mdash; no per-element class toggling
4. Chart.js colors are updated programmatically on toggle
5. Preference persisted in `localStorage` under key `taskflow_theme`

---

## Circular Progress Bar

The signature visual element is built with **pure SVG** and **CSS transitions**:

```
Circumference = 2 x PI x radius = 2 x 3.14159 x 75 = 471.24

stroke-dasharray:  471.24        (total dash length = full circle)
stroke-dashoffset: 471.24 * (1 - percent/100)

   0% complete  -->  offset = 471.24  (hidden)
  50% complete  -->  offset = 235.62  (half circle)
 100% complete  -->  offset = 0       (full circle)
```

The stroke uses an **SVG linearGradient** from Indigo (`#6366f1`) to Cyan (`#06b6d4`), creating a vibrant gradient ring. A 1-second `cubic-bezier` CSS transition smoothly animates changes.

---

## Charts

### Weekly Activity (Bar Chart)
- Shows tasks completed per day for the **last 7 days**
- Data sourced from the `completedAt` timestamp on each task
- Rounded bars (`borderRadius: 8`), no legend, custom tooltips

### Task Distribution (Doughnut Chart)
- Green (`#10b981`) for completed, Amber (`#f59e0b`) for pending
- 72% cutout for a clean ring aesthetic
- Graceful empty state: gray ring with "No tasks" label when no data

Both charts auto-update on every state change and adapt their colors for dark mode.

---

## Security

| Concern | Protection |
|:---|:---|
| **XSS** | All user input escaped via `escapeHtml()` before innerHTML rendering |
| **Injection** | No `eval()`, no `Function()`, no dynamic code execution |
| **Data scope** | localStorage only (same-origin), no external API calls |
| **CDN** | Chart.js loaded from jsdelivr; consider adding SRI hashes for production |

---

## Legacy Migration

Upgrading from the old version? **It's automatic.** On first load, the app detects the legacy `todos` key (plain string array) in localStorage, migrates each item to the new rich object format with `id`, `priority`, and timestamps, saves under the new `taskflow_todos` key, and removes the old key. Zero data loss.

---

## Documentation

A comprehensive **27-page architecture PDF** is included at [`docs/TaskFlow_Architecture.pdf`](docs/TaskFlow_Architecture.pdf). It covers:

- System architecture diagrams
- Data flow and state management
- HTML/CSS/JS layer deep dives
- Circular progress bar math
- Chart.js integration details
- Theme system internals
- Responsive breakpoint strategy
- Animation catalog
- Security & performance notes
- Developer guide for extending the app

To regenerate the PDF after making changes:

```bash
pip install fpdf2
python generate_docs.py
```

---

## Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Extension Ideas

- [ ] Due dates with calendar picker
- [ ] Drag-and-drop task reordering
- [ ] Task categories/tags
- [ ] Export tasks as JSON/CSV
- [ ] PWA support (offline mode + install)
- [ ] Subtasks / nested checklists
- [ ] Pomodoro timer integration
- [ ] Multi-board / project support

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

<div align="center">

**Built with vanilla web standards. No frameworks. No build tools. Just clean code.**

<br/>

Made with dedication by [**danialeyz**](https://github.com/danialeyz)

<br/>

If this project helped you, consider giving it a star!

**[Star this repo](https://github.com/danialeyz/todolist-project)**

</div>
