#!/bin/bash

# Creating a Python Virtual Environment
python3 -m venv .venv && \
    echo -e "\xE2\x9C\x85 Virtual Environment Created" || \
    (echo -e "\xE2\x9D\x8C Couldn't create Virtual Environment"; exit 1)

if [[ $? -eq 0 ]]; then
    # Activating the Virtual Environment
    source .venv/bin/activate && \
        echo -e "\xE2\x9C\x85 Virtual Environment Activated" || \
        (echo -e "\xE2\x9D\x8C Virtual Environment couldn't be activated" ; exit 1)

    if [[ $? -eq 0 ]]; then
        # Upgrading Pip, if necessary
        pip install --upgrade pip --quiet && \
            echo -e "\xE2\x9C\x85 Pip is up to date" || \
            (echo -e "\xE2\x9D\x8C Couldn't execute 'pip install --upgrade pip' " ; exit 1)

        if [[ $? -eq 0 ]]; then
            # Installing all essential Libraries
            pip install -r requirements.txt --quiet && \
                echo -e "\xE2\x9C\x85 All requirements installed! Ready to go!" || \
                (echo -e "\xE2\x9D\x8C Couldn't install the requirements"; exit 1)
        fi
    fi
fi