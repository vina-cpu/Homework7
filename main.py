import logging
from configure import configure_logging, configure_parser, make_directory, make_file_path
from generate_qr_code import make_qr

def main():
    configure_logging()
    args = configure_parser().parse_args()
    filepath = make_file_path()
    make_directory()
    make_qr(args.url, filepath)
    logging.info(f"QR code saved to {filepath.parent.name}/{filepath.stem}")

if __name__ == "__main__":
    main()