class Acciones{
    

    // obtener valores al actualizarlos en el modal de actualizar datos de el cliente
    obt_val_edi_cli(){
        let nombre =$("#nombre").val();
        let apellido =$("#apellido").val();
        let cedula = $("#cedula").val();
        let telefono =$("#telefono").val();
        let correo =$("#correo").val();
        let usuario = $("#usuario").val();
        let id_cli =$("#id_cli").val();
        ajax.editar_usuario_cliente("/val_camp_edi_cli", "POST", nombre, apellido, cedula, telefono, correo, usuario, id_cli);
    }
    


    // modal cambiar mi informaacion
    cam_inf_cli(){
            let modal="";
            modal+="<div class='modal-dialog modal1' id='mod1'>";
             modal+="<div class='modal-content px-2 py-2' id='mod_cuer'>";
             modal+="<div class'modal-header'>";
            modal+="<button type='button' class='btn btn-close bg-danger btn_cerrar_mod1 text-white'"; 
            modal+="data-bs-dismiss='modal' aria-label='Close'>x</button>";
            modal+="</div>";
            modal+="<div class='modal-body'>";
            modal+="<h2 class='text-center' id='id_tit_mod1'>Cambiar mi información</h2>";
            modal+="<form action=''>";
            modal+="<div class='mb-3'>";
             modal+="<label for='nombre' class='form-label'>Nombre:</label>";
             modal+="<input type='text'class='form-control'  id='nombre' name='nombre' autocomplete='off' maxlength='30'>";
             modal+="</div>";
             modal+="<div class='' id='error_nombre' name='error_nombre'></div>";
             modal+="<div class='mb-3'>";
             modal+="<label for='apellido' class='form-label'>Apellido:</label>";
             modal+="<input type='text'class='form-control'  id='apellido' name='apellido' autocomplete='off' maxlength='30'>";
             modal+="</div>";
             modal+="<div class='mb-3'>";
             modal+="<label for='usuario' class='form-label'>Usuario:</label>";
             modal+="<input type='text'class='form-control'  id='usuario' name='usuario' autocomplete='off' maxlength='30'>";
             modal+="</div>";
             modal+="<div class='' id='error_apellido' name='error_apellido'></div>";
             modal+="<div class='mb-3'>";
             modal+="<label for='cedula' class='form-label'>Cedula:</label>";
             modal+="<input type='number'class='form-control'  id='cedula' name='cedula' autocomplete='off' maxlength='10'>";
             modal+="</div>";
             modal+="<div class='' id='error_cedula' name='error_cedula'></div>";
             modal+="<div class='mb-3'>";
             modal+="<label for='telefono' class='form-label'>Telefono:</label>";
             modal+="<input type='number'class='form-control'  id='telefono' name='telefono' autocomplete='off' maxlength='11'>";
             modal+="</div>";
             modal+="<div class='' id='error_telefono' name='error_telefono'></div>";
             modal+="<div class='mb-3'>";
             modal+=`<label for="correo" class="form-label">Correo:</label>`;
             modal+=`<input type="email" class="form-control"  id="correo" name="correo" autocomplete='off' maxlength='40'>`;
             modal+="</div>";
             modal+="<div class='' id='error_correo' name='error_correo'></div>";
             modal+="<div class='mb-3'>";
             modal+=`<label for="usuario" class="form-label" id="lb_usuario" name="lb_usuario" style="display: none;">Usuario:</label>`;
             modal+=`<input type="text" class="form-control"  id="usuario" name="usuario" autocomplete='off' maxlength='40' style="display: none;">`;
             modal+=`<input type="text" class="form-control"  id="id_cli" name="id_cli" autocomplete='off' maxlength='40' style="display: none;">`;
             modal+="</div>";
             modal+=`<div class="modal-footer justify-content-center">`;
             modal+=`<button type="button" class="btn btn-danger"  id="agre_solicitar_exp" name="agre_solicitar_exp" onclick="acciones.edi_inf_cli()">Guardar</button>`;
             modal+="</div>";
             modal+=`<div class="mb-2" id="error_soli_exp1"></div>`;
             modal+="</form>";
             modal+="</div>";
             modal+="</div>";
             modal+="</div>";
             return modal;
    }
    // mostrar modal cambiar mi informacion como cliente
    mostrar_mod_inf_cli(){
        // $("#exampleModal1").html(acciones.cam_inf_cli());
        // $("#exampleModal1").modal("show");
        ajax.mostrar_modal_sn_para("/mos_inf_mod_cli", "POST", "", 4, acciones.cam_inf_cli())
        // ajax.mos_inf_mod_cli();
    }
    // EDITAR informacion propia como cliente
    edi_inf_cli(){
        let nombre =$("#nombre").val();
        let apellido =$("#apellido").val();
        let cedula = $("#cedula").val();
        let telefono = $("#telefono").val();
        let correo =$("#correo").val();
        let usuario = $("#usuario").val();
        ajax.editar_val_cli(nombre, apellido, cedula, telefono, correo, usuario);
    }
}
let acciones = new Acciones();