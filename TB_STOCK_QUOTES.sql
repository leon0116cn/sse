/*
Navicat MySQL Data Transfer

Source Server         : 172.19.16.233
Source Server Version : 50726
Source Host           : 172.19.16.233:3306
Source Database       : mydb

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2019-08-19 17:32:56
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for TB_STOCK_QUOTES
-- ----------------------------
DROP TABLE IF EXISTS `TB_STOCK_QUOTES`;
CREATE TABLE `TB_STOCK_QUOTES` (
  `serial_no` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '序号',
  `stock_code` varchar(255) NOT NULL COMMENT '证券代码',
  `stock_name` varchar(255) DEFAULT NULL COMMENT '证券简称',
  `open_price` decimal(10,2) DEFAULT NULL COMMENT '开盘',
  `high_price` decimal(10,2) DEFAULT NULL COMMENT '最高',
  `low_price` decimal(10,2) DEFAULT NULL COMMENT '最低',
  `last_price` decimal(10,2) DEFAULT NULL COMMENT '最新',
  `prev_price` decimal(10,2) DEFAULT NULL COMMENT '前收',
  `chg_rate` decimal(10,2) DEFAULT NULL COMMENT '涨跌幅',
  `volume` bigint(20) unsigned DEFAULT NULL COMMENT '成交量',
  `amount` bigint(20) unsigned DEFAULT NULL COMMENT '成交额',
  `trade_phase` varchar(255) DEFAULT NULL COMMENT '11',
  `chg_price` decimal(10,2) DEFAULT NULL COMMENT '涨跌',
  `amp_rate` decimal(10,2) DEFAULT NULL COMMENT '振幅',
  `cpxxsubtype` varchar(255) DEFAULT NULL COMMENT '类型,14',
  `cpxxprodusta` varchar(255) DEFAULT NULL COMMENT '12',
  `stock_total` int(11) DEFAULT NULL,
  `trade_date` date DEFAULT NULL,
  `trade_time` time DEFAULT NULL,
  PRIMARY KEY (`serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=3057 DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
