from flask import Flask, render_template, request
import pytest

import json
from tests.conftest import client

from server import (clubs, competitions)

valid_email = clubs[0]["email"]
invalid_email = "test@gmail.com"
    
# tests Login 
def test_login_valid_email(client):
    response = client.post("/showSummary", data={"email": valid_email})
    data = response.data.decode()
    assert valid_email in data
    assert response.status_code == 200
    assert request.path == "/showSummary"

    
def test_login_invalid_email(client):
    response = client.post("/showSummary", data={"email": invalid_email})
    data = response.data.decode()
    assert invalid_email not in data
    assert response.status_code == 200
    assert request.path == "/showSummary"

