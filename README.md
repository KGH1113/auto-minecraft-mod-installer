# Auto minecraft mod installer

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KGH1113/auto-minecraft-mod-installer.git
   cd auto-minecraft-mod-installer
   ```
2. Make venv environment
   ```bash
   python -m venv .venv
   ```
3. Activate venv

   ```bash
   # For Linux/Mac:
   source ./.venv/bin/bin/activate
   ```

   ```bash
   # For Windows:
   .\.venv\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the script:
   ```bash
   python main.py
   ```

## Customizing mod list

You can modify mods.py to customizing mod list you want to install.

- Each mods has to be separated by a line break.
- Mod name is only used when accessing "https://modrinth.com/mod/{MOD_NAME}" brings up the correct page.

## Licence

All rights reserved. See the [LICENSE](LICENSE.txt) file for more details.
