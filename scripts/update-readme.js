// This file updates the README.md file with content from README_TEMPLATE.md

const fs = require('fs');
const path = require('path');

const repoRoot = path.resolve(__dirname, '..');
const templatePath = path.join(__dirname, '../README_TEMPLATE.md');
const readmePath = path.join(repoRoot, 'README.md');

function updateReadme() {
    fs.readFile(templatePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading the template file:', err);
            return;
        }
        fs.writeFile(readmePath, data, 'utf8', (err) => {
            if (err) {
                console.error('Error writing to README.md:', err);
                return;
            }
            console.log('README.md has been updated successfully at repo root!');
        });
    });
}

updateReadme();