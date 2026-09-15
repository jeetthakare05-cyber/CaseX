console.log("CaseX JavaScript loaded!");

document.addEventListener("DOMContentLoaded", function () {

    const toasts = document.querySelectorAll(".toast");

    toasts.forEach((toast) => {

        // Auto remove after 4 seconds
        setTimeout(() => {

            toast.style.opacity = "0";
            toast.style.transform = "translateX(100px)";

            setTimeout(() => {
                toast.remove();
            }, 400);

        }, 4000);

        // Close button
        const closeBtn = toast.querySelector(".toast-close");

        closeBtn.addEventListener("click", function () {

            toast.style.opacity = "0";
            toast.style.transform = "translateX(100px)";

            setTimeout(() => {
                toast.remove();
            }, 400);

        });

    });

});