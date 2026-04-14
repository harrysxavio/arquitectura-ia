import unittest

from src.enums import Priority, RequestStatus, RequestType
from src.triage import initial_priority, next_status_for_owner


class TriageTest(unittest.TestCase):
    def test_security_requests_start_high(self) -> None:
        self.assertEqual(Priority.ALTA, initial_priority(RequestType.SEGURIDAD))

    def test_other_requests_start_low(self) -> None:
        self.assertEqual(Priority.BAJA, initial_priority(RequestType.OTRO))

    def test_owner_moves_request_to_assigned(self) -> None:
        self.assertEqual(RequestStatus.ASIGNADA, next_status_for_owner("coordinacion"))

    def test_missing_owner_keeps_request_in_triage(self) -> None:
        self.assertEqual(RequestStatus.EN_TRIAGE, next_status_for_owner(None))


if __name__ == "__main__":
    unittest.main()
