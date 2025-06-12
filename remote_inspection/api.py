"""Stub API for uploading geo-tagged photos and validating images."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import imghdr
from typing import Tuple, Optional, List, Dict


@dataclass
class PhotoRecord:
    """Record of an uploaded photo."""

    path: Path
    location: Tuple[float, float]
    metadata: Dict[str, object]


class PhotoInspectionAPI:
    """API for remote photo inspections."""

    def __init__(self) -> None:
        self.records: List[PhotoRecord] = []

    def upload_photo(self, path: str | Path, lat: float, lon: float) -> PhotoRecord:
        """Upload a photo with GPS coordinates.

        Parameters
        ----------
        path:
            File path to the image.
        lat, lon:
            Latitude and longitude.
        Returns
        -------
        PhotoRecord
            The stored photo record with validation metadata.
        """
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(p)

        img_type = imghdr.what(p)
        if img_type is None:
            raise ValueError("Unsupported image format")

        validation = {"valid": True, "format": img_type}
        ai_result = self._run_ai_analysis(p)

        record = PhotoRecord(path=p, location=(float(lat), float(lon)), metadata={
            "validation": validation,
            "ai": ai_result,
        })
        self.records.append(record)
        return record

    def _run_ai_analysis(self, path: Path) -> Optional[dict]:
        """Placeholder for vision model inference."""

        # Integrate computer vision models here (e.g., detect issues on site)
        return None
