from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from src.enums import Priority, RequestStatus, RequestType
from src.models import SupportRequest
from src.storage import JsonRequestStore


TEMP_ROOT = Path(__file__).resolve().parents[1] / ".test-tmp"


class JsonRequestStoreTest(unittest.TestCase):
    def test_load_missing_file_returns_empty_list(self) -> None:
        TEMP_ROOT.mkdir(exist_ok=True)
        with TemporaryDirectory(dir=TEMP_ROOT) as tempdir:
            store = JsonRequestStore(Path(tempdir) / "missing.json")

            self.assertEqual([], store.load())

    def test_save_and_load_roundtrip(self) -> None:
        TEMP_ROOT.mkdir(exist_ok=True)
        with TemporaryDirectory(dir=TEMP_ROOT) as tempdir:
            store = JsonRequestStore(Path(tempdir) / "requests.json")
            request = SupportRequest(
                id="req-test",
                title="Acceso VPN",
                description="Alta de acceso.",
                area="Operaciones",
                request_type=RequestType.ACCESO,
                priority=Priority.MEDIA,
                status=RequestStatus.EN_TRIAGE,
                created_at="2026-04-13T00:00:00Z",
                updated_at="2026-04-13T00:00:00Z",
            )

            store.save([request])
            loaded = store.load()

            self.assertEqual(1, len(loaded))
            self.assertEqual(request.id, loaded[0].id)
            self.assertEqual(request.request_type, loaded[0].request_type)


if __name__ == "__main__":
    unittest.main()
