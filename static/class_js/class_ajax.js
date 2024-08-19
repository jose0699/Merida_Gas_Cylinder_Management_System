class Ajax{
	tabla_bombonas(){
		$('#bombonas_persona').DataTable({
			"ajax":{
				"url": '/bombonas_todas',
				"type": "POST",
				"dataSrc":""
			},
			"columns":
			[
				{"data": "num"},
				{"data": "tamano_bombona"},
				{
                    "data": null
                    ,
                    orderable: true,
                    className: 'text-center',
                    render: function(data, type, row, meta) {
						if(row.id_estatus == 2){
							return "<div  class='d-flex align-items-center'><p class='mr-2'>"+ row.estatus +"</p><img style='width: 20px;' src='../static/icons/house-solid.svg'></div>";
						}else{
							return "<div  class='d-flex align-items-center'><p class='mr-2'>"+ row.estatus +"</p><img style='width: 20px;' src='../static/icons/bus-solid.svg'></div>";
						}
                        
                    }
                },
				{
                    "data": null
                    ,
                    orderable: true,
                    className: 'text-center',
					render: function(data, type, row, meta) {
						let actionButtons = "";
					
						if (row.id_estatus == 2) {
							actionButtons += `
								<div>
									<form action='/Inicio/Actualizar/Cilindro' method='POST'>
										<input type='hidden' name='id_bombon' id='id_bombon' value='${row.id_entrega_bombona}'>
										<button class='btn btn-primary btn-sm mr-1'>Actualizar Cilindro</button>
									</form>								
								</div>
								<div style='margin-top: 10px;'>
									<form action='eliminar_bombona' method='POST'>
										<input type='hidden' name='id_bombona' id='id_bombona' value='${row.id_entrega_bombona}'>
										<button class='btn btn-primary btn-sm mr-1'>Eliminar Cilindro</button>
									</form>
								</div>`;
						} else {
							actionButtons += ``;
						}
					
						return actionButtons;
					}
                }
                
			],
			ordering: true,
			language: {
				lengthMenu: "Mostrar _MENU_ registros por pagina",
				zeroRecords: "Ningun usuario encontrado",
				info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
				infoEmpty: "Ningun usuario encontrado",
				infoFiltered: "(filtrados desde _MAX_ registros totales)",
				search: "Buscar...",
				loadingRecords: "Cargando...",
				paginate: {
					first: "Primero",
					last: "Ultimo",
					next: "Siguiente",
					previous: "Anterior"
				}
			}
		});
	}


	///////////////////////////////////////////////////

	tabla_bombonas_dos(){
		$('#bombonas_persona').DataTable({
			"ajax":{
				"url": '/bombonas_todas',
				"type": "POST",
				"dataSrc":""
			},
			"columns":
			[
				{"data": "num"},
				{"data": "tamano_bombona"},
				{
                    "data": null
                    ,
                    orderable: true,
                    className: 'text-center',
                    render: function(data, type, row, meta) {
						if(row.id_estatus == 2){
							return "<div  class='d-flex align-items-center'><p class='mr-2'>"+ row.estatus +"</p><img style='width: 20px;' src='../static/icons/house-solid.svg'></div>";
						}else{
							return "<div  class='d-flex align-items-center'><p class='mr-2'>"+ row.estatus +"</p><img style='width: 20px;' src='../static/icons/bus-solid.svg'></div>";
						}
                        
                    }
                },
				{
                    "data": null
                    ,
                    orderable: true,
                    className: 'text-center',
					render: function(data, type, row, meta) {
						let actionButtons =`
							<div>
								<form action='/Administrador/Cilindro/Actualizar' method='POST'>
									<input type='hidden' name='id_bombon' id='id_bombon' value='${row.id_entrega_bombona}'>
									<button class='btn btn-primary btn-sm mr-1'>Actualizar Cilindro</button>
								</form>								
							</div>
							<div style='margin-top: 10px;'>
								<form action='/Administrador/Cilindro/5' method='POST'>
									<input type='hidden' name='id_bombona' id='id_bombona' value='${row.id_entrega_bombona}'>
									<button class='btn btn-primary btn-sm mr-1'>Eliminar Cilindro</button>
								</form>
							</div>`;
						
					
						return actionButtons;
					}
                }
                
			],
			ordering: true,
			language: {
				lengthMenu: "Mostrar _MENU_ registros por pagina",
				zeroRecords: "Ningun usuario encontrado",
				info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
				infoEmpty: "Ningun usuario encontrado",
				infoFiltered: "(filtrados desde _MAX_ registros totales)",
				search: "Buscar...",
				loadingRecords: "Cargando...",
				paginate: {
					first: "Primero",
					last: "Ultimo",
					next: "Siguiente",
					previous: "Anterior"
				}
			}
		});
	}

	///////////////////////////////////////////////////
	// editar mis valores como cliente (PARA REVISAR SI SE PUEDE REUTILIZAR)
	editar_val_cli(nombre, apellido, cedula, telefono, correo, usuario){
		$.ajax({
			url: "/guardar_cam_val_cli_mi",
			type: "POST",
			data: {
				nombre, apellido, cedula, telefono, correo, usuario
			},
			success: function(result){
				if(result == 1){
					window.location.href = '/inicio';
				}else if(result == 0){
					$("#error_soli_exp1").html(acciones.mos_men("danger", "Ha ocurrido un error"));
				}else{
					$("#error_soli_exp1").html(acciones.mos_men("danger", result));
				}		
			},
			error: function(error){
				console.log(error);
			}
		});
	}

///////////////////////////////////////////////////
///////////////////////////////////////////////////
persona_usuario() {
    let num_dos = 0;
    $('#persona_usuario').DataTable({
        "ajax": {
            "url": '/persona_usuario',
            "type": "POST",
            "dataSrc": ""
        },
        "columns": [
            {
                "data": null,
                "render": function (data, type, row, meta) {
                    return ++num_dos;
                }
            },
            {"data": "nombre"},
            {"data": "cedula"},
            {"data": "correo"},
            {
                "data": null,
                orderable: true,
                className: "text-center",
                render: function (data, type, row, meta) {
                    let actionButtons = "";
                    actionButtons += `
                        <div>
                            <form action='/Administrador/Cilindro' method='POST'>
                                <input type='hidden' name='vi_us' id='vi_us' value='${num_dos}'>
                                <button class='btn btn-primary btn-sm mr-1'>Visualizar Cilindro</button>
                            </form>
                        </div> 
                        <br>
                        <div>
                            <form action='/Administrador/Actualizar' method='POST'>
                                <input type='hidden' name='act_us' id='act_us' value='${row.cedula}'>
                                <button class='btn btn-primary btn-sm mr-1'>Actualizar Datos</button>
                            </form>
                        </div>
                    `;
                    return actionButtons;
                }
            }
        ],
        ordering: true,
        language: {
            lengthMenu: "Mostrar _MENU_ registros por pagina",
            zeroRecords: "Ningun usuario encontrado",
            info: "Mostrando de _START_ a _END_ de un total de _TOTAL_ registros",
            infoEmpty: "Ningun usuario encontrado",
            infoFiltered: "(filtrados desde _MAX_ registros totales)",
            search: "Buscar...",
            loadingRecords: "Cargando...",
            paginate: {
                first: "Primero",
                last: "Ultimo",
                next: "Siguiente",
                previous: "Anterior"
            }
        }
    });

    $.ajax({
        url: '/persona_usuario',
        type: 'POST',
        success: function (data) {
            console.log(data);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
        }
    });
}
	actualizar_tamano_bombona(url, type, data){

		$.ajax({
			url:url,
			type: type,
			data: {data},
			success: function(results){
				let array = ["opcion_vacio_tamano", "opcion_vacio_estatus"];
				let nv_array = [];

				if($("#tamano_bom").val() === ""){
					$("#opcion_vacio_tamano").html(acciones.mos_men('danger', 'El campo nombre esta vacio'));
					nv_array = array.filter(arr => arr !== 'tamano_bom');
					nv_array.forEach(element => {
						$(`#${element}`).html("");
					});
				}else if($("#nombre").val() === ""){
					$("#opcion_vacio_estatus").html(acciones.mos_men('danger', 'El campo nombre esta vacio'));
					nv_array = array.filter(arr => arr !== 'opcion_vacio_estatus');
					nv_array.forEach(element => {
						$(`#${element}`).html("");
					});
				}else{
					array.forEach(element => {
						$(`#${element}`).html("");
					});
					let fk_tamano = $("#fk_tamano").val();
					let fk_estatus = $("#fk_estatus");
					let id_bom = $("#id_bom").val();
					ajax.actualizar_tamano('/actualizar_tamano', 'GET', fk_tamano, fk_estatus, id_bom)
				}
			}
		})

	}

	actualizar_tamano(url, type, fk_tamano, fk_estatus_bombona, id_bom){
        $.ajax({
			url: url,
			type: type,
			data: {
				url, type, fk_tamano, fk_estatus_bombona, id_bom
			},
			success: function(result){
				window.location.href = '/inicio';
			},
			error: function(error){
				console.log(error);
			}
		});
	}
	
}
	


let ajax = new Ajax();