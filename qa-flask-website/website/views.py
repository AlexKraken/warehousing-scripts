from flask import Blueprint, render_template, request, jsonify, flash, session
from check_weight import check_weight
from typing import Optional
from . import db
from .models import Barcode
import json

views = Blueprint("views", __name__)


def get_all_barcodes() -> list[Barcode]:
    return Barcode.query.all()


def get_barcode_by_id(barcode_id: str) -> Optional[Barcode]:
    return Barcode.query.get(barcode_id)


@views.route("/", methods=["GET", "POST"])
@views.route("/barcode", methods=["GET", "POST"])
def barcode_logger():
    message_found: str = ""
    message_added: str = ""

    if request.method == "POST":
        barcode: str = request.form.get("barcode")

        if request.form.get("action") == "check-barcode":
            barcode_found: Optional[Barcode] = Barcode.query.get(barcode)
            session["barcode"]: Optional[str] = request.form.get("barcode")

            if barcode_found:
                message_found = "Barcode found!"
            else:
                message_found = "Barcode not found!"

        elif request.form.get("action") == "add-barcode":
            barcode_found: Optional[Barcode] = Barcode.query.get(session["barcode"])

            if barcode_found:
                message_added = "Barcode already added!"
            elif session["barcode"]:
                notes = request.form.get("notes")
                new_barcode = Barcode(id=session["barcode"], notes=notes)
                message_added = "Barcode added!"
                db.session.add(new_barcode)
                db.session.commit()

    barcodes: list[Barcode] = Barcode.query.all()

    return render_template(
        "barcode-logger.html",
        message_found=message_found,
        message_added=message_added,
        barcodes=barcodes,
    )


@views.route("/weight", methods=["GET", "POST"])
def weight_checker():
    absolute_error, percentage_error, measured_weight, expected_weight = 0.0, 0.0, 0.0, 0.0

    if request.method == "POST":
        measured_weight = (float)(request.form.get("measured-weight"))
        expected_weight = (float)(request.form.get("expected-weight"))
        absolute_error, percentage_error = map(lambda x: round(x, 2), check_weight(expected_weight, measured_weight))

    return render_template(
        "weight-checker.html",
        absolute_error=absolute_error,
        percentage_error=percentage_error,
        measured_weight=measured_weight,
        expected_weight=expected_weight,
    )


@views.route("/delete-barcode", methods=["POST"])
def delete_barcode():
    print(request)
    barcode = Barcode.query.get(json.loads(request.data)["barcode"])

    if barcode:
        db.session.delete(barcode)
        db.session.commit()

    return jsonify({})
