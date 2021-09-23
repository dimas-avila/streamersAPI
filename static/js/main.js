async function fetchStreamer(streamer){

    let streamers = await fetch(
        "/api/searchstreamer",
        {
            method: "POST",
            body: streamer
        }
    )

    streamers = await streamers.json()

    return streamers
}

function updateTable(data) {
    console.log(data["name"])

    document.getElementById("nombre").innerHTML = data["name"]
    document.getElementById("subs").innerHTML = data["subs"]
    document.getElementById("followers").innerHTML = data["followers"]
    
}


const form = document.getElementById("searchform")
form.addEventListener("submit", (e) => {
    e.preventDefault()
    let formData = new FormData(form)
    fetchStreamer(formData).then(
        (res) =>{
            updateTable(res)
        }
    )
})