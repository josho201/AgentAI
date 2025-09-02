# 1. Instala dependencias
sudo apt update
sudo apt install -y curl gnupg software-properties-common

# 2. Importa la clave GPG de GitHub
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
  sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg

sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

# 3. Agrega el repositorio oficial de GitHub CLI
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \ sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# 4. Instala gh
sudo apt update
sudo apt install -y gh
