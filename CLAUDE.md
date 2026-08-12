# PersonaOS

## Overview

PersonaOS is a modern desktop system monitor inspired by Persona 3 Reload.

The application is built with:

- Python 3.12
- PySide6
- Qt Style Sheets (QSS)
- psutil
- pyqtgraph

The goal is to create a beautiful desktop dashboard that feels like a Persona game UI while remaining lightweight and modular.

---

# Design Philosophy

Priorities:

1. Clean architecture
2. Modular services
3. Smooth animations
4. High FPS
5. Minimal CPU usage
6. Easy extensibility

Avoid unnecessary complexity.

---

# Architecture

src/personaos/

core/
Application startup.

services/
Background services that collect data.

monitoring/
Monitoring logic.

ui/
Qt widgets and pages.

themes/
QSS themes.

utils/
Reusable helper classes.

assets/
Fonts, icons, sounds, images.

---

# Coding Standards

Prefer:

- dataclasses
- pathlib
- type hints
- composition over inheritance
- small classes
- readable code

Avoid:

- giant files
- duplicated code
- circular imports
- hardcoded paths

---

# UI Rules

The UI should always feel like Persona 3 Reload.

Animations should be:

- smooth
- subtle
- responsive

Cards should have:

- rounded corners
- consistent spacing
- consistent typography
- matching accent colors

---

# Services

Each monitoring service should:

- run independently
- be restartable
- never block the UI
- emit signals instead of directly updating widgets

---

# Performance

Target:

60 FPS

CPU usage should remain minimal.

Avoid unnecessary polling.

Reuse widgets whenever possible.

---

# Theme

Primary colors:

- Dark blue
- Cyan
- White

Avoid random colors.

Follow Persona branding.

---

# Project Goals

Future features:

- Plugin system
- Weather
- GitHub dashboard
- Docker monitoring
- Minecraft server monitoring
- Network monitor
- Calendar
- Notes
- AI assistant integration

---

# Assistant Guidelines

When modifying code:

- Preserve architecture.
- Keep widgets modular.
- Prefer reusable components.
- Do not rewrite working code without reason.
- Explain major architectural changes.
