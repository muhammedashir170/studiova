# Use official Odoo 18 image
FROM odoo:18.0

# Copy your theme into custom addons path
COPY ./addons /mnt/extra-addons

# Set file permissions
RUN chmod -R 755 /mnt/extra-addons

# Expose Odoo’s default port
EXPOSE 8069

# Run Odoo with your theme addons
CMD ["odoo", "-d", "demo_db", "--addons-path=/usr/lib/python3/dist-packages/odoo/addons,/mnt/extra-addons", "--db-filter=demo_db"]
