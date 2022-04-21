function CampServer2() {
    let a2 = document.getElementById('s1').value;

    let a3 = document.getElementById('s2').value;

    window.location.href = `/Camp/${a2}/${a3}`;
}