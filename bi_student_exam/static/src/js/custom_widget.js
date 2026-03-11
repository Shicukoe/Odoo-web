/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState, onMounted, onWillUpdateProps } from "@odoo/owl";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Many2OneField } from "@web/views/fields/many2one/many2one_field";

// Custom Student information widget
export class StudentInfoWidget extends Component {
    setup(){
        this.orm = useService("orm");
        this.state = useState({
            student: null
        });
        onMounted(() => {
        this.loadStudent(this.props.value);
        });

        onWillUpdateProps((nextProps) => {
            if(nextProps.value !== this.props.value){
                this.loadStudent(nextProps.value);
            }
        });
    }
    
    async loadStudent(){
        const value = this.props.record.data.student_id;
        const student_id = Array.isArray(value) ? value[0] : value;

        if(!student_id){
            this.state.student = null;
            return;
        }

        const data = await this.orm.read(
            "bi_student_exam.student",
            [student_id],
            ["class_name","phone","guardian_email"]
        );
        this.state.student = data.length ? data[0] : null;
    }

    async refreshInfo(){
        await this.loadStudent();
    }

    async generateAttachment(){
        const id = this.props.record.resId;

        if(!id){
            alert("Please save the record first");
            return;
        }

        await this.orm.call(
            "bi_student_exam.student_exam",
            "action_generate_attachment",
            [[id]]
        );

    }

}

StudentInfoWidget.template = "bi_student_exam.StudentInfoWidget";
StudentInfoWidget.components = { Many2OneField };
StudentInfoWidget.supportedFieldTypes = ["many2one"];
StudentInfoWidget.props = standardFieldProps;
registry.category("fields").add("student_info_widget",StudentInfoWidget);

// Custom Color Widget
class CustomColor extends Component {}
CustomColor.template = "bi_student_exam.CustomColor";
CustomColor.supportedFieldTypes = ["float"];
registry.category("fields").add("custom_color", CustomColor);