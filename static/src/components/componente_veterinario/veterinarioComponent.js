import { registry } from '@web/core/registry';
import { Component, useState, onWillStart, useRef } from 'web.core';
import { useService } from '@web/core/utils/hooks';

class VeterinarioComponent extends Component {
    setup() {
        this.state = useState({
            veterinario: {
                idVeterinario: "",
                nombre: "",
                apellidos: "",
                especialidad: ""
            },
            isEdit: false,
            activeId: false,
            veterinarioList: []
        });

        this.orm = useService("orm");
        this.model = "veterinariaupo.veterinario";
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllVeterinarios();
        });
    }

    async getAllVeterinarios() {
        this.state.veterinarioList = await this.orm.searchRead(this.model, [], ["idVeterinario", "nombre", "apellidos", "especialidad"]);
    }

    addVeterinario() {
        this.resetForm();
        this.state.activeId = false;
        this.state.isEdit = false;
        $('#veterinarioModal').modal('show');
    }

    editVeterinario(veterinario) {
        this.state.activeId = veterinario.id;
        this.state.isEdit = true;
        this.state.veterinario = { ...veterinario };
        $('#veterinarioModal').modal('show');
    }

    async saveVeterinario() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.veterinario]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.veterinario);
        }
        $('#veterinarioModal').modal('hide');
        this.resetForm();
        await this.getAllVeterinarios();
    }

    resetForm() {
        this.state.veterinario = {
            idVeterinario: "",
            nombre: "",
            apellidos: "",
            especialidad: ""
        };
    }

    async deleteVeterinario(veterinario) {
        await this.orm.unlink(this.model, [veterinario.id]);
        await this.getAllVeterinarios();
    }

    async searchVeterinarios() {
        const text = this.searchInput.el.value;
        this.state.veterinarioList = await this.orm.searchRead(this.model, [['idVeterinario', 'ilike', text]], ["idVeterinario", "nombre", "apellidos", "especialidad"]);
    }
}

VeterinarioComponent.template = 'owl.VeterinarioComponent';
registry.category('actions').add('owl.action_VeterinarioComponent_js', VeterinarioComponent);
