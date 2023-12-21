import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class ClienteComponent extends Component {
    setup() {
        this.state = useState({
            cliente: {
                dni: "",
                nombre: "",
                apellidos: "",
                direccion: "",
                telefono: "",
                correo: ""
            },
            isEdit: false,
            activeId: false,
            clienteList: []
        });

        this.orm = useService("orm");
        this.model = "veterinariaupo.cliente";
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllClientes();
        });
    }

    async getAllClientes() {
        this.state.clienteList = await this.orm.searchRead(this.model, [], ["dni", "nombre", "apellidos"]);
    }

    addCliente() {
        this.resetForm();
        this.state.activeId = false;
        this.state.isEdit = false;
        $('#clienteModal').modal('show');
    }

    editCliente(cliente) {
        this.state.activeId = cliente.id;
        this.state.isEdit = true;
        this.state.cliente = { ...cliente };
        $('#clienteModal').modal('show');
    }

    async saveCliente() {
        if (!this.state.isEdit) {
            await this.orm.create(this.model, [this.state.cliente]);
            this.resetForm();
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.cliente);
        }
        $('#clienteModal').modal('hide');
        this.resetForm();
        await this.getAllClientes();
    }

    resetForm() {
        this.state.cliente = {
            dni: "",
            nombre: "",
            apellidos: "",
            direccion: "",
            telefono: "",
            correo: ""
        };
    }

    async deleteCliente(cliente) {
        await this.orm.unlink(this.model, [cliente.id]);
        await this.getAllClientes();
    }

    async searchClientes() {
        const text = this.searchInput.el.value;
        this.state.clienteList = await this.orm.searchRead(this.model, [['dni', 'ilike', text]], ["dni", "nombre", "apellidos"]);
    }
}

ClienteComponent.template = 'owl.ClienteComponent';
registry.category('actions').add('owl.action_ClienteComponent_js', ClienteComponent);
