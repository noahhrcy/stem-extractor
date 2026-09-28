# Stem Extractor

Spicetify extension that adds a button to **extract the stems** (vocals / drums /
bass / other) of the track you're listening to, right from Spotify.

On click, a menu lets you **tick the stems** you want and optionally **download
the full track** (MP3). Tracks run one after another in a **queue** with a
progress bar, estimated time left, and the ability to cancel.

## ⚠️ Requires SpiceUtils

Stem separation runs on a **local server** provided by the **SpiceUtils**
application (Python + Demucs). The extension alone is not enough.

➡️ **Download SpiceUtils:** https://github.com/noahhrcy/SpiceUtils/releases

Once SpiceUtils is installed and open (its server starts with the app), the
button works. If the server isn't detected, the extension offers the download
link. SpiceUtils also re-applies Spicetify automatically after Spotify updates,
so the button doesn't disappear.

## Usage

- Button in the playbar, or right-click on a track.
- Stems are saved to the folder configured in SpiceUtils (default
  `Downloads/Stems`).

## License

MIT.
