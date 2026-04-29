# Safari_testing_web

remmina -c vnc://localhost:5901

docker-compose logs -f

docker compose exec playwright-safari python3 tests/interactive_safari.py
___________________________________________________________________________________
sudo apt --purge autoremove -y
sudo apt clean
sudo apt autoclean -y

rm -rf ~/.cache/thumbnails/*
rm -rf ~/.local/share/Trash/*/**
sudo rm -rf /tmp/* /var/tmp/*
sudo rm -rf /var/cache/fontconfig/
sudo rm -rf /var/cache/man/

rm -rf ~/.cache/google-chrome/*
rm -rf ~/.config/Code/CachedData/* и rm -rf ~/.config/Code/User/workspaceStorage/*
__________________________________________________________________________________________
Установите Lighthouse глобально: npm install -g lighthouse
Запустите аудит: lighthouse https://example.com --output=json --output=html --output-path=./report.html
__________________________________________________________________________________________