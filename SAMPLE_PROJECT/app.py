"""CLI for the SAMPLE_PROJECT support desk example."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.enums import RequestType
from src.reporter import format_request, format_request_list
from src.service import RequestNotFoundError, SupportDeskService


DEFAULT_DATA_PATH = Path(__file__).parent / "data" / "requests.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Mesa interna de soporte operativo - ejemplo funcional."
    )
    parser.add_argument(
        "--data",
        default=str(DEFAULT_DATA_PATH),
        help="Ruta del JSON runtime. Default: data/requests.json",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("demo", help="Ejecuta un flujo pequeno de ejemplo.")

    create = subparsers.add_parser("create", help="Crea una solicitud.")
    create.add_argument("--title", required=True)
    create.add_argument("--description", required=True)
    create.add_argument("--area", required=True)
    create.add_argument(
        "--type",
        required=True,
        choices=[request_type.value for request_type in RequestType],
    )
    create.add_argument("--owner", default=None)

    subparsers.add_parser("list", help="Lista solicitudes.")

    close = subparsers.add_parser("close", help="Cierra una solicitud por id.")
    close.add_argument("--id", required=True)
    close.add_argument("--note", required=True)

    return parser


def run_demo(service: SupportDeskService) -> str:
    created = service.create_request(
        title="Revisar acceso a VPN",
        description="Equipo de operaciones necesita validar acceso antes del turno.",
        area="Operaciones",
        request_type=RequestType.ACCESO,
        owner="coordinacion",
    )
    security = service.create_request(
        title="Alerta de credenciales",
        description="Se reporta posible exposicion de credenciales internas.",
        area="Seguridad",
        request_type=RequestType.SEGURIDAD,
    )
    closed = service.close_request(
        created.id,
        "Acceso revisado y solicitud resuelta.",
    )
    return "\n".join(
        [
            "Demo ejecutado.",
            "",
            "Solicitud cerrada:",
            format_request(closed),
            "",
            "Solicitud de seguridad en triage:",
            format_request(security),
        ]
    )


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    service = SupportDeskService.from_path(Path(args.data))

    try:
        if args.command == "demo":
            print(run_demo(service))
            return 0

        if args.command == "create":
            request = service.create_request(
                title=args.title,
                description=args.description,
                area=args.area,
                request_type=args.type,
                owner=args.owner,
            )
            print(format_request(request))
            return 0

        if args.command == "list":
            print(format_request_list(service.list_requests()))
            return 0

        if args.command == "close":
            request = service.close_request(args.id, args.note)
            print(format_request(request))
            return 0
    except (RequestNotFoundError, ValueError) as exc:
        parser.exit(status=1, message=f"Error: {exc}\n")

    parser.error(f"Comando no soportado: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
