<div align="center">

# Keyboard Event Lab

A workspace for typing, inspecting keyboard events and exporting a session, available in the browser and as a Python desktop application.

<a href="https://enybyy.github.io/keyboard-event-lab/"><img src="docs/media/demo.svg" width="360" alt="Open demo"></a>

<p><a href="https://github.com/Enybyy"><img src="docs/media/github.svg" width="112" alt="Eliud Rojas Mendoza on GitHub"></a>
<a href="https://www.linkedin.com/in/eliud-rojas-mendoza-414652212/"><img src="docs/media/linkedin.svg" width="112" alt="Eliud Rojas Mendoza on LinkedIn"></a>
<a href="https://www.upwork.com/freelancers/~01471ca462b236e8e5"><img src="docs/media/upwork.svg" width="112" alt="Eliud Rojas Mendoza on Upwork"></a></p>

[![Keyboard Event Lab in use](assets/screenshots/keyboard-desktop.png)](https://enybyy.github.io/keyboard-event-lab/)

*Actual laboratory screenshot. Recording is limited to its own typing area.*

[About](#about-the-project) · [Workflow](#everyday-workflow) · [Technology](#built-with) · [Run locally](#local-use)

</div>


## About the project

Text in an input field does not show how each keystroke was received. Keyboard Event Lab places a typing area beside a visual keyboard and event console, making the relationship between typed text and application events visible.

Recording starts explicitly, can be paused and keeps a bounded session. JSON export allows events to be reviewed outside the lab when exploring input behavior or testing interactions. The Python version provides the same kind of workspace in its own window.

## Everyday workflow

| Inside the project | Detail |
| --- | --- |
| Visible input | Explicitly started recording within the app's own typing area. |
| Event inspection | Key, physical code, modifiers, repeat and action in the web version. |
| Session controls | Start, pause, clear and bounded event history. |
| Export | JSON session for review outside the laboratory. |
| Desktop version | Python/Tkinter application recording key presses in its own window. |

## Explore the demo

The interface uses Spanish labels:

1. Select **Iniciar registro** (Start recording) and type in the test area.
2. Inspect the key, physical code and keydown/keyup action.
3. Select **Pausar** (Pause), **Limpiar eventos** (Clear events) or **Exportar JSON** (Export JSON).

The web version keeps the latest 2,000 events, including modifiers, timestamps and repeat state. The Python version records key presses with key name, character and timestamp. Controls and other windows are excluded. Information stays in memory unless you choose to export it.

## Scope

This project replaces the suite's former `KeyLogger` with a visible input laboratory. It does not use global hooks, `pynput`, monitoring of other applications, data transmission or hidden execution. Closing the page or window ends the session. Use sample text.

Browsers do not report every operating-system shortcut. The illustrated keyboard covers letters, space, Enter and Backspace; the console can display other events delivered by the browser. Paste, dictation and IME input can insert text without one keystroke per character.

## Built with

| Area | Technology |
| --- | --- |
| Web demo | HTML, CSS and JavaScript |
| Desktop application | Python and Tkinter |
| Sessions | In-memory history and JSON export |
| Verification | unittest and Playwright |

## Local use

<details>
<summary><strong>Run on your computer</strong></summary>

The public demo needs no installation. To serve the repository locally:

```powershell
python -m http.server 5086 --bind 127.0.0.1
```

Open `http://127.0.0.1:5086`. The desktop version requires Python 3.12+ with Tkinter:

```powershell
python app.py
```

Tkinter is included in the usual Python installer for Windows. Some Linux distributions require their Tk package to be installed separately.

</details>

<details>
<summary><strong>Tests</strong></summary>

```powershell
python -m unittest discover -s tests -v
```

Tests cover start/pause, history bounds, sequence, clearing and Unicode export. `scripts/browser-test.cjs` uses Playwright to check typing, pause, control exclusion, export and responsive layout, and captures the application.

</details>

---

<div align="center">

**Eliud Rojas Mendoza · Enybyy**

<p><a href="https://github.com/Enybyy"><img src="docs/media/github.svg" width="112" alt="Eliud Rojas Mendoza on GitHub"></a>
<a href="https://www.linkedin.com/in/eliud-rojas-mendoza-414652212/"><img src="docs/media/linkedin.svg" width="112" alt="Eliud Rojas Mendoza on LinkedIn"></a>
<a href="https://www.upwork.com/freelancers/~01471ca462b236e8e5"><img src="docs/media/upwork.svg" width="112" alt="Eliud Rojas Mendoza on Upwork"></a></p>

</div>
