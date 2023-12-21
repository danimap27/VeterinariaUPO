import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class ATSComponent extends Component {
    setup() {
        this.state = useState({
            ats: {
                idATS: "",
                especialidad: "",
                estado: "",
                dni: "",
                nombre: "",
                apellidos: ""
            },
            isEdit: false,
            activeId: false,
        });

        this.orm = useService("orm");
        this.model = "veterinariaupo.ats";
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllATS();
        });
    }

    async getAllATS() {
        this.state.atsList = await this.orm.searchRead(this.model, [], ["idATS", "especialidad", "estado"]);
    }

    addATS() {
        this.resetForm();
        this.state.activeId = false;
        this.state.isEdit = false;
        $('#atsModal').modal('show');
    }

    editATS(ats) {
        this.state.activeId = ats.id;
        this.state.isEdit = true;
        this.state.ats = { ...ats };
        $('#atsModal').modal('show');
    }

    async saveATS() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.ats]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.ats);
        }
        $('#atsModal').modal('hide');
        this.resetForm();
        await this.getAllATS();
    }

    resetForm() {
        this.state.ats = {
            idATS: "",
            especialidad: "",
            estado: "",
            dni: "",
            nombre: "",
            apellidos: ""
        };
    }

    async deleteATS(ats) {
        await this.orm.unlink(this.model, [ats.id]);
        await this.getAllATS();
    }

    async searchATS() {
        const text = this.searchInput.el.value;
        this.state.atsList = await this.orm.searchRead(this.model, [['idATS', 'ilike', text]], ["idATS", "especialidad", "estado"]);
    }
}

ATSComponent.template = 'owl.ATSComponent';
registry.category('actions').add('owl.action_ATSComponent_js', ATSComponent);
