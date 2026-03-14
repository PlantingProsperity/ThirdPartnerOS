"""
Partner OS — Audio Transcription (OpenAI Whisper, CPU mode)
=============================================================
Transcribes audio files (.m4a, .mp3, .mp4, .wav) using OpenAI Whisper
running entirely on CPU. The GTX 580 (Fermi, nouveau driver) cannot
run Whisper on GPU — CPU mode is the correct and only option here.

Transcription output is saved as a .md file in the deal jacket
transcripts/ directory alongside the original audio file.

Model selection: the "base" Whisper model is recommended for the
i7-950 hardware. "small" is the practical maximum. "medium" and
larger will be prohibitively slow on this CPU.

Usage:
    from src.integrations.whisper_transcriber import transcribe_audio
    from pathlib import Path
    transcript_path = transcribe_audio(
        audio_path=Path("/path/to/field_recording.m4a"),
        deal_id=42,
    )
"""

from pathlib import Path

from config import DealSubdir
from src.utils.logger import get_logger

log = get_logger(__name__)

WHISPER_MODEL: str = "base"
"""
Whisper model to use for transcription.
Options: tiny, base, small, medium, large.
"base" recommended for the i7-950. "small" is the maximum practical size.
"""


def transcribe_audio(audio_path: Path, deal_id: int) -> Path:
    """
    Transcribe an audio file to text using Whisper (CPU mode only).

    Saves output as {original_stem}.md in the deal jacket transcripts/
    directory. Returns the path to the generated transcript file.

    Args:
        audio_path: Absolute path to the audio file to transcribe.
        deal_id: Database ID of the deal this audio belongs to.

    Returns:
        Absolute path to the generated .md transcript file.

    Raises:
        FileNotFoundError: If audio_path does not exist.
        RuntimeError: If Whisper transcription fails.
    """
    raise NotImplementedError("transcribe_audio() is not yet implemented.")
