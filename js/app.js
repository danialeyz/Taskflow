// ===== Constants =====
const STORAGE_KEY = "taskflow_todos";
const THEME_KEY = "taskflow_theme";

// ===== State =====
let todos = [];
let weeklyChart = null;
let statusChart = null;

// ===== DOM References =====
const $ = (sel) => document.querySelector(sel);

const el = {
  addForm: $("#add-form"),
  taskInput: $("#task-input"),
  priorityGroup: $("#priority-group"),
  tasksList: $("#tasks-list"),
  searchInput: $("#search-input"),
  filterStatus: $("#filter-status"),
  filterPriority: $("#filter-priority"),
  clearCompleted: $("#clear-completed"),
  emptyState: $("#empty-state"),
  circleProgress: $("#circle-progress"),
  circlePercent: $("#circle-percent"),
  statTotal: $("#stat-total"),
  statDone: $("#stat-done"),
  statPending: $("#stat-pending"),
  headerDate: $("#header-date"),
  themeToggle: $("#theme-toggle"),
  weeklyCanvas: $("#weekly-chart"),
  statusCanvas: $("#status-chart"),
};

// ===== Utilities =====
function generateId() {
  return Date.now().toString(36) + Math.random().toString(36).substr(2, 9);
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function formatDate(dateStr) {
  const d = new Date(dateStr);
  return d.toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

function getSelectedPriority() {
  const checked = el.priorityGroup.querySelector("input:checked");
  return checked ? checked.value : "medium";
}

// ===== Local Storage =====
function loadTodos() {
  const data = localStorage.getItem(STORAGE_KEY);
  if (data) return JSON.parse(data);

  // Migrate from legacy format (plain string array)
  const legacy = localStorage.getItem("todos");
  if (legacy) {
    try {
      const items = JSON.parse(legacy);
      const migrated = items.map((text) => ({
        id: generateId(),
        text: typeof text === "string" ? text : String(text),
        completed: false,
        priority: "medium",
        createdAt: new Date().toISOString(),
        completedAt: null,
      }));
      saveTodos(migrated);
      localStorage.removeItem("todos");
      return migrated;
    } catch (e) {
      console.warn("Failed to migrate legacy todos:", e);
    }
  }

  return [];
}

function saveTodos(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data || todos));
}

// ===== Todo CRUD =====
function addTodo(text, priority) {
  const todo = {
    id: generateId(),
    text,
    completed: false,
    priority,
    createdAt: new Date().toISOString(),
    completedAt: null,
  };
  todos.unshift(todo);
  saveTodos();
  render();
}

function toggleTodo(id) {
  const todo = todos.find((t) => t.id === id);
  if (!todo) return;
  todo.completed = !todo.completed;
  todo.completedAt = todo.completed ? new Date().toISOString() : null;
  saveTodos();
  render();
}

function deleteTodo(id) {
  todos = todos.filter((t) => t.id !== id);
  saveTodos();
}

function clearCompleted() {
  const items = el.tasksList.querySelectorAll(".task-item.completed");
  if (items.length === 0) return;

  items.forEach((item) => item.classList.add("slide-out"));

  setTimeout(() => {
    todos = todos.filter((t) => !t.completed);
    saveTodos();
    render();
  }, 350);
}

// ===== Filtering & Search =====
function getFilteredTodos() {
  const search = el.searchInput.value.toLowerCase().trim();
  const status = el.filterStatus.value;
  const priority = el.filterPriority.value;

  return todos.filter((todo) => {
    const matchSearch = !search || todo.text.toLowerCase().includes(search);
    const matchStatus =
      status === "all" ||
      (status === "active" && !todo.completed) ||
      (status === "completed" && todo.completed);
    const matchPriority = priority === "all" || todo.priority === priority;
    return matchSearch && matchStatus && matchPriority;
  });
}

// ===== Rendering =====
function createTaskElement(todo) {
  const li = document.createElement("li");
  li.className = "task-item" + (todo.completed ? " completed" : "");
  li.dataset.id = todo.id;

  li.innerHTML = `
    <button class="task-check" aria-label="${todo.completed ? "Mark incomplete" : "Mark complete"}">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="20 6 9 17 4 12"/>
      </svg>
    </button>
    <div class="task-content">
      <p class="task-text">${escapeHtml(todo.text)}</p>
      <div class="task-meta">
        <span class="priority-badge priority-${todo.priority}">${capitalize(todo.priority)}</span>
        <span class="task-date">${formatDate(todo.createdAt)}</span>
      </div>
    </div>
    <button class="task-delete" aria-label="Delete task">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="3 6 5 6 21 6"/>
        <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>
      </svg>
    </button>
  `;

  return li;
}

function renderTasks() {
  const filtered = getFilteredTodos();
  el.tasksList.innerHTML = "";

  filtered.forEach((todo) => {
    el.tasksList.appendChild(createTaskElement(todo));
  });

  el.emptyState.classList.toggle("visible", filtered.length === 0);
}

function updateStats() {
  const total = todos.length;
  const done = todos.filter((t) => t.completed).length;
  const pending = total - done;
  const percent = total ? Math.round((done / total) * 100) : 0;

  // Stat cards
  el.statTotal.textContent = total;
  el.statDone.textContent = done;
  el.statPending.textContent = pending;

  // Circular progress bar
  const circumference = 2 * Math.PI * 75; // r = 75
  const offset = circumference * (1 - percent / 100);
  el.circleProgress.style.strokeDashoffset = offset;
  el.circlePercent.textContent = percent + "%";
}

function render() {
  renderTasks();
  updateStats();
  updateCharts();
}

// ===== Chart.js Integration =====
function getWeeklyData() {
  const labels = [];
  const data = [];

  for (let i = 6; i >= 0; i--) {
    const date = new Date();
    date.setHours(0, 0, 0, 0);
    date.setDate(date.getDate() - i);

    labels.push(
      date.toLocaleDateString("en-US", { weekday: "short" })
    );

    const nextDay = new Date(date);
    nextDay.setDate(nextDay.getDate() + 1);

    const count = todos.filter((t) => {
      if (!t.completedAt) return false;
      const d = new Date(t.completedAt);
      return d >= date && d < nextDay;
    }).length;

    data.push(count);
  }

  return { labels, data };
}

function getChartColors() {
  const isDark = document.documentElement.dataset.theme === "dark";
  return {
    gridColor: isDark ? "rgba(148, 163, 184, 0.08)" : "rgba(0, 0, 0, 0.06)",
    textColor: isDark ? "#94a3b8" : "#64748b",
  };
}

function initCharts() {
  if (typeof Chart === "undefined") return;

  const colors = getChartColors();
  const weeklyData = getWeeklyData();

  // Weekly Activity Bar Chart
  weeklyChart = new Chart(el.weeklyCanvas.getContext("2d"), {
    type: "bar",
    data: {
      labels: weeklyData.labels,
      datasets: [
        {
          label: "Completed",
          data: weeklyData.data,
          backgroundColor: "rgba(99, 102, 241, 0.75)",
          borderColor: "rgba(99, 102, 241, 1)",
          borderWidth: 2,
          borderRadius: 8,
          borderSkipped: false,
          maxBarThickness: 32,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          backgroundColor: "rgba(15, 23, 42, 0.9)",
          titleFont: { family: "Inter", size: 12 },
          bodyFont: { family: "Inter", size: 12 },
          padding: 10,
          cornerRadius: 8,
          displayColors: false,
          callbacks: {
            label: (ctx) =>
              ctx.parsed.y === 1
                ? "1 task completed"
                : ctx.parsed.y + " tasks completed",
          },
        },
      },
      scales: {
        x: {
          grid: { display: false },
          ticks: {
            color: colors.textColor,
            font: { family: "Inter", size: 11, weight: 500 },
          },
          border: { display: false },
        },
        y: {
          beginAtZero: true,
          grid: { color: colors.gridColor },
          ticks: {
            color: colors.textColor,
            font: { family: "Inter", size: 11 },
            stepSize: 1,
            padding: 8,
          },
          border: { display: false },
        },
      },
    },
  });

  // Task Status Doughnut Chart
  const done = todos.filter((t) => t.completed).length;
  const pending = todos.length - done;
  const hasData = done > 0 || pending > 0;

  statusChart = new Chart(el.statusCanvas.getContext("2d"), {
    type: "doughnut",
    data: {
      labels: hasData ? ["Completed", "Pending"] : ["No tasks"],
      datasets: [
        {
          data: hasData ? [done, pending] : [1],
          backgroundColor: hasData
            ? ["#10b981", "#f59e0b"]
            : [colors.gridColor],
          borderWidth: 0,
          cutout: "72%",
          spacing: hasData ? 3 : 0,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: "bottom",
          labels: {
            color: colors.textColor,
            font: { family: "Inter", size: 12, weight: 500 },
            padding: 20,
            usePointStyle: true,
            pointStyleWidth: 10,
          },
        },
        tooltip: {
          backgroundColor: "rgba(15, 23, 42, 0.9)",
          titleFont: { family: "Inter", size: 12 },
          bodyFont: { family: "Inter", size: 12 },
          padding: 10,
          cornerRadius: 8,
          displayColors: true,
          callbacks: {
            label: (ctx) => {
              if (!hasData) return "Add tasks to see distribution";
              const total = done + pending;
              const pct = total
                ? Math.round((ctx.parsed / total) * 100)
                : 0;
              return " " + ctx.label + ": " + ctx.parsed + " (" + pct + "%)";
            },
          },
        },
      },
    },
  });
}

function updateCharts() {
  if (!weeklyChart || !statusChart) return;

  // Weekly chart
  const weeklyData = getWeeklyData();
  weeklyChart.data.labels = weeklyData.labels;
  weeklyChart.data.datasets[0].data = weeklyData.data;
  weeklyChart.update("none");

  // Doughnut chart
  const done = todos.filter((t) => t.completed).length;
  const pending = todos.length - done;
  const hasData = done > 0 || pending > 0;
  const colors = getChartColors();

  statusChart.data.labels = hasData ? ["Completed", "Pending"] : ["No tasks"];
  statusChart.data.datasets[0].data = hasData ? [done, pending] : [1];
  statusChart.data.datasets[0].backgroundColor = hasData
    ? ["#10b981", "#f59e0b"]
    : [colors.gridColor];
  statusChart.data.datasets[0].spacing = hasData ? 3 : 0;
  statusChart.update("none");
}

// ===== Theme =====
function initTheme() {
  const saved = localStorage.getItem(THEME_KEY);
  if (saved) {
    document.documentElement.dataset.theme = saved;
  }
}

function toggleTheme() {
  const current = document.documentElement.dataset.theme;
  const next = current === "dark" ? "light" : "dark";
  document.documentElement.dataset.theme = next;
  localStorage.setItem(THEME_KEY, next);

  // Update chart colors for new theme
  if (weeklyChart && statusChart) {
    const colors = getChartColors();

    weeklyChart.options.scales.x.ticks.color = colors.textColor;
    weeklyChart.options.scales.y.ticks.color = colors.textColor;
    weeklyChart.options.scales.y.grid.color = colors.gridColor;
    weeklyChart.update();

    statusChart.options.plugins.legend.labels.color = colors.textColor;

    // Update "no data" background color
    const done = todos.filter((t) => t.completed).length;
    const pending = todos.length - done;
    if (done === 0 && pending === 0) {
      statusChart.data.datasets[0].backgroundColor = [colors.gridColor];
    }
    statusChart.update();
  }
}

// ===== Event Handlers =====
function handleAddTask(e) {
  e.preventDefault();
  const text = el.taskInput.value.trim();

  if (!text) {
    el.taskInput.focus();
    el.taskInput.parentElement.classList.add("shake");
    setTimeout(() => el.taskInput.parentElement.classList.remove("shake"), 500);
    return;
  }

  addTodo(text, getSelectedPriority());
  el.taskInput.value = "";
  el.taskInput.focus();
}

function handleTaskClick(e) {
  const deleteBtn = e.target.closest(".task-delete");
  const checkBtn = e.target.closest(".task-check");
  const taskItem = e.target.closest(".task-item");

  if (!taskItem) return;

  if (deleteBtn) {
    const id = taskItem.dataset.id;
    taskItem.classList.add("slide-out");
    taskItem.addEventListener("animationend", () => {
      deleteTodo(id);
      render();
    });
  } else if (checkBtn) {
    toggleTodo(taskItem.dataset.id);
  }
}

// ===== Initialization =====
function init() {
  // Set today's date in the header
  const now = new Date();
  el.headerDate.textContent = now.toLocaleDateString("en-US", {
    weekday: "long",
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  // Load theme preference
  initTheme();

  // Load todos from storage
  todos = loadTodos();

  // Initial render
  renderTasks();
  updateStats();

  // Initialize charts
  try {
    initCharts();
  } catch (err) {
    console.warn("Charts could not be initialized:", err);
  }

  // Event listeners
  el.addForm.addEventListener("submit", handleAddTask);
  el.tasksList.addEventListener("click", handleTaskClick);
  el.searchInput.addEventListener("input", renderTasks);
  el.filterStatus.addEventListener("change", renderTasks);
  el.filterPriority.addEventListener("change", renderTasks);
  el.clearCompleted.addEventListener("click", clearCompleted);
  el.themeToggle.addEventListener("click", toggleTheme);

  // PWA: register service worker
  if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("./sw.js", { scope: "./" }).catch(() => {});
  }
}

document.addEventListener("DOMContentLoaded", init);
