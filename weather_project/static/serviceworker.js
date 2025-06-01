// serviceworker.js

self.addEventListener('install', function (e) {
    console.log('[ServiceWorker] Installed');
    self.skipWaiting(); // Optional: activates the service worker immediately
});

self.addEventListener('activate', function (e) {
    console.log('[ServiceWorker] Activated');
    return self.clients.claim(); // Optional: ensures the SW controls all clients ASAP
});

self.addEventListener('fetch', function (e) {
    console.log('[ServiceWorker] Fetching', e.request.url);
    // You can add caching logic here later if needed
});
