const form = document.getElementById('registerForm');
    const message = document.getElementById('message');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
      };

      try {
        const response = await fetch('/api/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // if CSRF is enforced
          },
          body: JSON.stringify(formData),
        });

        const data = await response.json();
        if (response.ok) {
          message.innerHTML = `<span style="color: green;">✅ ${data.message}</span>`;
          form.reset();
        } else {
          message.innerHTML = `<span style="color: red;">❌ ${data.error || JSON.stringify(data)}</span>`;
        }
      } catch (error) {
        message.innerHTML = `<span style="color: red;">❌ Network error</span>`;
      }
    });