BASE_URL = "http://127.0.0.1:8000";


function generate_components_suite(data) {
	suites = data.suites;
	for (let index = 0; index < suites.length; index++) {
		var element = data.suites[index];
		document.getElementById("suites").innerHTML += `<div>
        <div
            class="xt-card p-7 sm:p-9 text-base rounded-2xl text-gray-900 xt-links-default bg-gray-100"
            id="suite-${index}"
            >
            
            <div class="xt-h4">${element}</div>
            <p>
                ${data[element]["doc"]}
            </p>
        </div>
    </div>`;
	}

    for (let index = 0; index < suites.length; index++) {
        var element = data.suites[index];

        for (let button_index = 0; button_index < data[element]["package"].length; button_index++) {
            document.getElementById(`suite-${index}`).innerHTML += `<button type="button" id="${suites[index]}-${button_index}"
            class="xt-button py-2.5 px-3.5 text-sm rounded-md font-medium leading-snug tracking-wider uppercase text-gray-900 bg-gray-100 transition hover:bg-gray-200 active:bg-gray-300 on:bg-gray-200">
            ${data[element]["package"][button_index]}
        </button>`

            console.log(`${suites[index]}-${button_index}`)
            document.getElementById(`${suites[index]}-${button_index}`).addEventListener(
                'click', function(e){
                    document.getElementById("command").innerHTML = `<div>
                    <div
                        class="xt-card p-7 sm:p-9 text-base rounded-2xl text-gray-900 xt-links-default bg-gray-100"
                        id="command-${suites[index]}-${button_index}"
                        >
                        <div class="xt-h4">${data[element]["package"][button_index]}</div>
                        <p>test</p>
                    </div>

                    <div></div>
                </div>`
                }
            )


        }
    }
}

async function makePostRequest(url, data) {
	try {
		const response = await fetch(url, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(data),
		});
		const responseData = await response.json();
		return responseData;
	} catch (error) {
		console.error(error);
	}
}

const url = `${BASE_URL}/fetch_script`;
const data = {
	key: "default",
};

window.addEventListener(
	"load",
	makePostRequest(url, data).then((responseData) => {
		generate_components_suite(responseData);
		console.log(responseData);
	})
);
