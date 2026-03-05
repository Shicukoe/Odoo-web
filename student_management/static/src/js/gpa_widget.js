/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

class GPAColor extends Component {}

GPAColor.template = "student_management.GPAColor";

registry.category("fields").add("gpa_color", GPAColor);