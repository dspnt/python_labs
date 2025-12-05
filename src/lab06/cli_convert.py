def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()

    if not argv or any(arg in argv for arg in ("-h", "--help")):
        parser.print_help()
        return

    args = parser.parse_args(argv)

    command_handlers = {
        "json2csv": json_to_csv,
        "csv2json": csv_to_json,
        "csv2xlsx": csv_to_xlsx,
    }

    try:
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")

        command_handlers[args.command](args.input, args.output)
        print(f"Файл создан: {args.output}")

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        sys.exit(1)
