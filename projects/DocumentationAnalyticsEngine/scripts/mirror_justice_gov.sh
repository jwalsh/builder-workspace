#!/bin/bash

# Set the URL to mirror
URL="https://www.justice.gov/atr/us-and-plaintiff-states-v-google-llc-2023-trial-exhibits"

# Create a timestamp for the archive
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Set the directory for storing mirrors
MIRROR_DIR="data/mirrors/$TIMESTAMP"

# Create the mirror directory
mkdir -p "$MIRROR_DIR"

# Use wget to mirror the site
wget --mirror \
     --convert-links \
     --adjust-extension \
     --page-requisites \
     --no-parent \
     --directory-prefix="$MIRROR_DIR" \
     --no-host-directories \
     --restrict-file-names=windows \
     "$URL"

echo "Mirroring complete. Files saved in $MIRROR_DIR"
