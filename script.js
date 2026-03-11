async function searchCar() {
    try {
        const response = await fetch(
            "https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvaluesextended/1HGCM82633A004352?format=json"
        );
        const data = await response.json();
        const car = data.Results[0];

        const marca = car.Make || "Desconhecida";
        const modelo = car.Model || "Desconhecido";
        const ano = car.ModelYear || "Desconhecido";
        const trim = car.Trim || "";

        const carInfo = `${marca} ${modelo} ${ano} ${trim}`;

        // Mostrar informações básicas
        document.getElementById("vinCar").innerHTML = carInfo;

        // Mostrar imagem usando Placehold.co (grátis)
        document.getElementById("carImage").src = `https://placehold.co/400x200?text=${encodeURIComponent(carInfo)}`;

    } catch (error) {
        console.error("Erro ao buscar informações do carro:", error);
        document.getElementById("vinCar").innerHTML = "Erro ao buscar informações do carro.";
        document.getElementById("carImage").src = "";
    }
}