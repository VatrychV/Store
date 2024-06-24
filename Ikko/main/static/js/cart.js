     // Функція для оновлення замовлення або кількості товару
     function updateCart(productId, action) {
        var url = '/update_item/';

        var data = {
            'productId': productId,
            'action': action
        };

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getToken('csrftoken')
            },
            body: JSON.stringify(data)
        })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Відповідь від сервера:', data);
          location.reload(); // Оновлюємо сторінку для оновлення даних з корзини
        })
        .catch((error) => {
            console.error('Помилка:', error);
            // Обробка помилок
        });
    }

    // Отримати всі кнопки і додати обробник подій для кожної
    var allButtons = document.querySelectorAll('.update-cart, .chg-quantity');

    allButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            var productId = this.dataset.product;
            var action = this.dataset.action;
            console.log('productId:', productId, 'Action:', action);

            updateCart(productId, action);
        });
    });