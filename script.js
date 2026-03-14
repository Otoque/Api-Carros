async function searchCar() {
    try {

        const response = await fetch("http://127.0.0.1:8000/carros/aleatorio");
        const car = await response.json();

        // IDENTIFICAÇÃO
        const identificacao = {
            vin: car.vin || "Desconhecido",
            marca: car.marca || "Desconhecida",
            modelo: car.modelo || "Desconhecido",
            ano: car.anoModelo || "Desconhecido",
            serie: car.serie || "",
            trim: car.trim || "",
            tipo: car.tipoVeiculo || "Desconhecido",
            imagem: car.imagem || "Sem imagem :("
        };

        // MOTOR
        const motor = {
            modelo: car.modeloMotor || "Desconhecido",
            configuracao: car.configuracaoMotor || "Desconhecido",
            cilindros: car.numeroCilindros || "Desconhecido"
        };

        // POTÊNCIA
        const potencia = {
            hp: car.potenciaHP || "Desconhecido",
            kw: car.potenciaKW || "Desconhecido"
        };

        // CILINDRADA
        const cilindrada = {
            litros: car.cilindradaL || "Desconhecido",
            cc: car.cilindradaCC || "Desconhecido",
            polegadas: car.cilindradaPC || "Desconhecido"
        };

        // COMBUSTÍVEL
        const combustivel = {
            principal: car.principalCombustivel || "Desconhecido",
            secundario: car.secundarioCombustivel || "Nenhum"
        };

        // FABRICANTE
        const fabricante = {
            nome: car.fabricante_obj?.nomeFabricante || "Desconhecido",
            cidade: car.fabricante_obj?.cidadeFabricante || "Desconhecido",
            estado: car.fabricante_obj?.estadoFabricante || "Desconhecido",
            pais: car.fabricante_obj?.paisFabricante || "Desconhecido"
        };

        // TEXTO PRINCIPAL DO CARRO
        const carInfo = `
        VIN: ${identificacao.vin} 
        Marca: ${identificacao.marca}  
        Modelo: ${identificacao.modelo} 
        Tipo: ${identificacao.tipo} 
        Serie: ${identificacao.serie} 
        Ano: ${identificacao.ano}  
        Trim: ${identificacao.trim}`;

        // MOTOR INFO
        const motorInfo = `
        Motor: ${motor.modelo} | ${motor.cilindros} cilindros`;

        // POTÊNCIA
        const potenciaInfo = `
        Potência: ${potencia.hp} HP (${potencia.kw} kW)`;

        // COMBUSTÍVEL
        const combustivelInfo = `
        Combustível: ${combustivel.principal}`;

        // FABRICANTE
        const fabricanteInfo = `
        Fabricante: ${fabricante.nome} - ${fabricante.pais}`;

        // MOSTRAR NA TELA
        document.getElementById("vinCar").innerText = carInfo;
        document.getElementById("motorCar").innerText = motorInfo;
        document.getElementById("potenciaCar").innerText = potenciaInfo;
        document.getElementById("combustivelCar").innerText = combustivelInfo;
        document.getElementById("fabricanteCar").innerText = fabricanteInfo;

        // IMAGEM PLACEHOLDER
        const query = `${identificacao.marca} ${identificacao.modelo} car`;

        document.getElementById("carImage").src = identificacao.imagem;

    } catch (error) {
        console.error("Erro ao buscar carro:", error);
        document.getElementById("vinCar").innerText = "Erro ao carregar carro";
    }
}