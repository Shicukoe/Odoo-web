/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Many2OneField } from "@web/views/fields/many2one/many2one_field";
import { useService } from "@web/core/utils/hooks";
import { Component } from "@odoo/owl";

export class StudentInfoWidget extends Many2OneField {

    setup() {
        super.setup();
        this.orm = useService("orm");
    }

    async refreshInfo() {
        if (!this.props.value) return;

        const student = await this.orm.read(
            "bi_student_exam.student",
            [this.props.value[0]],
            ["class_name", "phone", "guardian_email"]
        );

        this.studentInfo = student[0];
        this.render();
    }

    async generateAttachment() {
        if (!this.props.record.resId) {
            alert("Please save record first");
            return;
        }

        await this.orm.call(
            "bi_student_exam.student_exam",
            "action_generate_attachment",
            [this.props.record.resId]
        );
    }
}

StudentInfoWidget.template = "bi_student_exam.StudentInfoWidget";

registry.category("fields").add("student_info_widget", StudentInfoWidget);
