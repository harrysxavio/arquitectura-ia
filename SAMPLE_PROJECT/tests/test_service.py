from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from src.enums import Priority, RequestStatus, RequestType
from src.service import RequestNotFoundError, SupportDeskService


TEMP_ROOT = Path(__file__).resolve().parents[1] / ".test-tmp"


class SupportDeskServiceTest(unittest.TestCase):
    def make_service(self) -> SupportDeskService:
        TEMP_ROOT.mkdir(exist_ok=True)
        self.tempdir = TemporaryDirectory(dir=TEMP_ROOT)
        self.addCleanup(self.tempdir.cleanup)
        return SupportDeskService.from_path(Path(self.tempdir.name) / "requests.json")

    def test_create_request_persists_and_applies_security_priority(self) -> None:
        service = self.make_service()
        request = service.create_request(
            title="Credenciales expuestas",
            description="Revisar posible exposicion.",
            area="Seguridad",
            request_type=RequestType.SEGURIDAD,
        )

        self.assertEqual(Priority.ALTA, request.priority)
        self.assertEqual(RequestStatus.EN_TRIAGE, request.status)
        self.assertEqual([request.id], [item.id for item in service.list_requests()])

    def test_create_request_with_owner_is_assigned(self) -> None:
        service = self.make_service()
        request = service.create_request(
            title="Acceso VPN",
            description="Alta de acceso para turno.",
            area="Operaciones",
            request_type="acceso",
            owner="coordinacion",
        )

        self.assertEqual(RequestStatus.ASIGNADA, request.status)
        self.assertEqual("coordinacion", request.owner)

    def test_close_request_requires_existing_id(self) -> None:
        service = self.make_service()

        with self.assertRaises(RequestNotFoundError):
            service.close_request("req-nope", "No existe")

    def test_close_request_requires_note(self) -> None:
        service = self.make_service()
        request = service.create_request(
            title="Acceso VPN",
            description="Alta de acceso.",
            area="Operaciones",
            request_type="acceso",
        )

        with self.assertRaises(ValueError):
            service.close_request(request.id, " ")

    def test_close_request_updates_status_and_note(self) -> None:
        service = self.make_service()
        request = service.create_request(
            title="Acceso VPN",
            description="Alta de acceso.",
            area="Operaciones",
            request_type="acceso",
        )

        closed = service.close_request(request.id, "Resuelto")

        self.assertEqual(RequestStatus.CERRADA, closed.status)
        self.assertEqual("Resuelto", closed.closing_note)


if __name__ == "__main__":
    unittest.main()
