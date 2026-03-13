async function searchCar() {
    try {

        const response = await fetch("http://127.0.0.1:8000/carros/aleatorio");
        const car = await response.json();

        const marca = car.marca || "Desconhecida";
        const modelo = car.modelo || "Desconhecido";
        const ano = car.anoModelo || "Desconhecido";
        const trim = car.trim || "";
        const modeloMotor = car.modeloMotor || "Desconhecido";
        const combustivel = car.principalCombustivel || "Desconhecido";

        const carInfo = `${marca} ${modelo} ${ano} ${trim}`;

        const motorInfo = `Motor: ${modeloMotor} | Combustível: ${combustivel}`;

        // Mostrar nome do carro
        document.getElementById("vinCar").innerText = carInfo;

        // Mostrar informações do motor
        document.getElementById("motorCar").innerText = motorInfo;

        // Imagem placeholder
        document.getElementById("carImage").src =
        `https://placehold.co/400x200?text=${encodeURIComponent(carInfo)}`;

    } catch (error) {
        
    }
}