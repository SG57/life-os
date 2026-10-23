> **For your assistant.** Life OS pointer · Framework version: 3.6.0 · Where the department catalog lives.

# Department catalog

The catalog is `dist/CATALOG.txt`, built from the department files in `areas/` by `tools/build-paste.py`: every department, its default (on, opt-in, or asleep until a life event), what wakes it, and what it touches. Each department's rules, standing watch, red flags, and intake questions are its AREA message, `dist/AREA-<key>.txt`.

At setup (BOOTSTRAP B10) each department is sorted into one of three lists: build (the life map touches it), asleep (with its wake trigger), or not applicable (never built). Seed each built department from its AREA message only (D2); never from this page or from memory.
