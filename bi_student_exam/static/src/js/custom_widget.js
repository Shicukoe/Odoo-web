/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Many2OneField } from "@web/views/fields/many2one/many2one_field";
import { useService } from "@web/core/utils/hooks";
import { useState } from "@odoo/owl";
import { Component } from "@odoo/owl";

// Custom Student information widget
export class StudentInfoWidget extends Many2OneField {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.state = useState({
            studentInfo: null,
        });
    }
    async refreshInfo() {
        if (!this.props.value) {
            this.state.studentInfo = null;
            return;
        }

        const studentId = this.props.value[0];

        const result = await this.orm.read(
            "bi_student_exam.student",
            [studentId],
            ["class_name", "phone", "guardian_email"]
        );

        if (result.length) {
            this.state.studentInfo = result[0];
        }
    }

    async generateAttachment() {

        const recordId = this.props.record.resId;

        if (!recordId) {
            alert("Please save the exam record first.");
            return;
        }

        await this.orm.call(
            "bi_student_exam.student_exam",
            "action_generate_attachment",
            [recordId]
        );

        alert("Attachment generated.");
    }
}

StudentInfoWidget.template = "bi_student_exam.StudentInfoWidget";
registry.category("fields").add("student_info_widget",StudentInfoWidget);

// Custom Color Widget
class CustomColor extends Component {}
CustomColor.template = "bi_student_exam.CustomColor";
registry.category("fields").add("custom_color", CustomColor);