$(document).ready(function(){
    let expire = document.getElementById('expire')
    let perishable = document.getElementById("perishable")
    perishable.addEventListener("change", (elem) => {
        if(elem.target.value == 2){
            expire.parentElement.classList.add("dnone")
            expire.removeAttribute("required");
            expire.value = null;
            return;
        }
        expire.parentElement.classList.remove("dnone")
        expire.setAttribute("required", "required")
    })
    
})

function changeBtn(){
    const btn = document.getElementById("sendButton")
    const salesInput = document.getElementById("sales")
    const quantityInput = document.getElementById("quantity")
    const salesSpan = document.getElementById("salesSpan")
    const quantitySpan = document.getElementById("quantitySpan")
    console.log(salesInput.value, parseInt(quantitySpan.innerHTML, 10), parseInt(quantityInput.value,10))
    if(parseInt(quantityInput.value,10)){
        console.log("entrouaqui")
    if((salesInput.value) <= parseInt(quantitySpan.innerHTML, 10) + parseInt(quantityInput.value,10)){
        if(quantityInput.value == "" && salesInput.value == "")
            return
        btn.removeAttribute("disabled")
        return
    }}
    else{
        console.log("entrouelse")
        if((salesInput.value) <= parseInt(quantitySpan.innerHTML, 10)){
            if(quantityInput.value == "" && salesInput.value == "")
                return
            btn.removeAttribute("disabled")
            return
    }
}
    btn.setAttribute("disabled", "disabled")
}