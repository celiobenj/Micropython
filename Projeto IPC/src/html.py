class html():
    def page() -> str:
        return """
<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Controle LED</title>
    <script src="https://jscolor.com/release/2.5.2/jscolor.js"></script>
    <style>
        body {
            text-align: center;
            font-family: monospace;
            margin: 0;
            padding: 0;
        }


        .tab {
            display: none;
        }

        .tab.active {
            display: block;
        }

        .tab-buttons {
            display: flex;
            justify-content: space-between;
            margin: 0;
            padding: 0;
        }

        .tab-buttons button {
            flex: 1;
            background-color: white;
            border: none;
            padding: 20px;
            cursor: pointer;
            font-size: 16px;

            font-family: monospace;
        }

        .tab-buttons button:hover {
            background-color: #f0f0f0;
        }

        #colorTab svg {
            width: 100px;
            height: 100px;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 10px auto;
        }

        #colorTab svg #cor {
            fill: #000
        }

        #colorTab h1 {
            margin: 20px 0;
            font-family: monospace;
        }

        #cicloButtonList,
        #transitionButtonList {
            list-style-type: none;
            padding: 0;            
            margin: 0;             
        }

        #cicloButtonList li,
        #transitionButtonList li {
            margin: 10px 0; 
        }

        #cicloTab button#cicle1,
        #transitionTab button#transition {
            color: white;
            font-size: 24px;
            padding: 15px 30px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: blue;
            font-family: monospace;
        }

        #cicloTab button#cicle1:hover,
        #transitionTab button#transition:hover {
            background-color: darkblue;
        }

        #cicloTab h1,
        #transitionTab h1 {
            margin: 20px 0;
        }

        #cicloTab form,
        #transitionTab form {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            margin: 20px auto;
            max-width: 500px;
            padding: 0 20px 0 20px;
        }

        #cicloTab form h2,
        #transitionTab h2 {
            align-items: end;
            margin: 0;
        }

        #cicloTab form input,
        #cicloTab form textarea,
        #transitionTab input {
            margin: 5px 0;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
            border: 1px solid #ccc;
            width: -webkit-fill-available;
            max-width: 500px;
            font-family: monospace;
        }

        #cicloTab form textarea {
            height: 100px;
            resize: none;
        }

        #cicloTab form button,
        #transitionTab button {
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            background-color: blue;
            color: white;
            cursor: pointer;
            font-family: monospace;
            margin: 0px auto;
        }

        #cicloTab form button:hover,
        #transitionTab button:hover {
            background-color: darkblue;
        }

        @media (max-width: 250px) {
            .tab-buttons {
                flex-direction: column;
            }

            .tab-buttons button {
                margin-bottom: 10px;
            }

            #cicloTab form input,
            #cicloTab form textarea {
                width: calc(100% - 20px);
            }
        }
    </style>
</head>

<body>
    <div class="tab-buttons">
        <button type="button" onclick="showTab('colorTab')">Color Input</button>
        <button type="button" onclick="showTab('cicloTab')">Ciclo</button>
        <button type="button" onclick="showTab('transitionTab')">Transição</button>
    </div>

    <div id="colorTab" class="tab active">
        <h1>Selecione uma cor</h1>

        <svg fill="#000000" height="800px" width="800px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512" xml:space="preserve">
            <g>
                <g id="cor">
                    <path d="M395.636,302.545h-58.182v-58.182c0-6.982-4.655-11.636-11.636-11.636h-23.273l20.945-27.927
                            c3.491-4.655,2.327-12.8-2.327-16.291s-12.8-2.327-16.291,2.327l-34.909,46.545c-2.327,3.491-3.491,8.145-1.164,11.636
                            S274.618,256,279.273,256h34.909v46.545H197.818v-93.091h46.545l-20.945,27.927c-3.491,4.655-2.327,12.8,2.327,16.291
                            s12.8,2.327,16.291-2.327l34.909-46.545c2.327-3.491,3.491-8.145,1.164-11.636s-5.818-6.982-10.473-6.982h-81.455
                            c-6.982,0-11.636,4.655-11.636,11.636v104.727c-6.982,0-11.636,4.655-11.636,11.636s4.655,11.636,11.636,11.636h221.091
                            c6.982,0,11.636,4.655,11.636,11.636c0,6.982-4.655,11.636-11.636,11.636H116.364c-6.982,0-11.636-4.655-11.636-11.636
                            c0-6.982,4.655-11.636,11.636-11.636H128c11.636,0,11.636-10.473,11.636-18.618V139.636c0-64,52.364-116.364,116.364-116.364
                            s116.364,52.364,116.364,116.364v128c0,6.982,4.655,11.636,11.636,11.636s11.636-4.655,11.636-11.636v-128
                            C395.636,62.836,332.8,0,256,0S116.364,62.836,116.364,139.636c0,0,0,123.345,0,162.909c-19.782,0-34.909,15.127-34.909,34.909
                            c0,19.782,15.127,34.909,34.909,34.909h279.273c19.782,0,34.909-15.127,34.909-34.909
                            C430.545,317.673,415.418,302.545,395.636,302.545z" />
                </g>
            </g>
            <g>
                <g>
                    <path d="M186.182,395.636c-6.982,0-11.636,4.655-11.636,11.636v93.091c0,6.982,4.655,11.636,11.636,11.636
        s11.636-4.655,11.636-11.636v-93.091C197.818,400.291,193.164,395.636,186.182,395.636z" />
                </g>
            </g>
            <g>
                <g>
                    <path d="M325.818,395.636c-6.982,0-11.636,4.655-11.636,11.636v93.091c0,6.982,4.655,11.636,11.636,11.636
        s11.636-4.655,11.636-11.636v-93.091C337.455,400.291,332.8,395.636,325.818,395.636z" />
                </g>
            </g>
        </svg>
        <p>Cor selecionada</p>

        <input id="colorInput" data-jscolor="" onchange="update_color()">
    </div>

    <div id="cicloTab" class="tab">
        <h1>Selecione um ciclo</h1>
        <ul id="cicloButtonList">
            <li><button id="cicle1" type="button" onclick="cicle(1)">Ciclo 1</button></li>
            <li><button id="cicle1" type="button" onclick="cicle(2)">Ciclo 2</button></li>
            <li><button id="cicle1" type="button" onclick="cicle(3)">Ciclo 3</button></li>
        </ul>
        <form id="customizationCicloForm">
            <h2>Faça um ciclo personalizado: </h2>
            <input type="number" id="delayCicle" placeholder="Delay(ms)" required>
            <textarea id="hex_list" placeholder="Cores personalizadas"></textarea>
            <br>
            <button type="button" onclick="cicle()">Enviar</button>
        </form>
    </div>

    <div id="transitionTab" class="tab">
        <h1>Ative o efeito de <i>transição</i> dos LEDs</h1>
        <ul id="transitionButtonList">
            <li><button id="transition" type="button" onclick="transition(50)">Transição rápida</button></li>
            <li><button id="transition" type="button" onclick="transition(100)">Transição normal</button></li>
            <li><button id="transition" type="button" onclick="transition(250)">Transição lenta</button></li>
        </ul>
        <form id="customizationTransitionForm">
            <h2>Escolha um tempo personalizado: </h2>
            <input type="number" id="delayTransition" placeholder="Delay(ms)" required>
            <br>
            <button type="button" onclick="transition()">Enviar</button>
        </form>
    </div>

    <script>
        jscolor.presets.default = {
            format: 'rgb', 
            shadow: false,
            width: 250,
            palette: [
                '#000000',
                '#FFFFFF',
                '#FF0000',
                '#FFFF00',
                '#00FF00',
                '#00FFFF',
                '#0000FF',
                '#FF00FF',
            ],
        };

        let picker = new JSColor('#colorInput');

        function showTab(tabId) {
            let tabs = document.querySelectorAll('.tab');
            tabs.forEach(tab => {
                tab.classList.remove('active');
            });
            document.getElementById(tabId).classList.add('active');
        }

        function update_color() {
            var cor = picker.toRGBString();
            document.getElementById('cor').style.fill = cor;

            let rgb = cor.match(/\d+/g);

            let r = parseInt(rgb[0]);
            let g = parseInt(rgb[1]);
            let b = parseInt(rgb[2]);

            let data = JSON.stringify({ "type": "update_color", r, g, b });
            console.log(data)
            post(data);
        };

        function cicle(preset = 0) {
            let delay = document.getElementById('delayCicle').value;
            let hex_list = document.getElementById('hex_list').value;

            if (preset == 0){
                if (delay.trim() === '' || isNaN(delay)) {
                    alert('Insira um número em Delay');
                    return false;
                }
            }

            let data = JSON.stringify({ 
                "type": "cicle", 
                preset, 
                delay,
                hex_list
            });
            console.log(data);
            post(data);
        }

        function transition(delay) {
            
            if (!delay){
                delay = document.getElementById('delayTransition').value;
            }
            console.log(delay)
            console.log(typeof(delay))

            let data = JSON.stringify({ 
                "type": "transition",
                delay
            });
            console.log(data)
            post(data);
        };

        function post(data) {
            fetch('/result', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: data
            })
                .then(response => response.json())
                .then(data => {
                    console.log(data);
                })
                .catch(error => {
                    console.error('Erro:', error);
                });
        };
    </script>
</body>
</html>
    """